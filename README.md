# Google Assistant Secondary

A Home Assistant custom component that registers a **second** Google Assistant Smart Home fulfillment endpoint, fully independent from the built-in `google_assistant` integration.

This lets two different Google accounts each control a different set of HA devices on a single Home Assistant instance.

## How it works

| | Primary (built-in) | Secondary (this component) |
|---|---|---|
| **Domain** | `google_assistant` | `google_assistant_secondary` |
| **Fulfillment URL** | `/api/google_assistant` | `/api/google_assistant_secondary` |
| **YAML key** | `google_assistant:` | `google_assistant_secondary:` |
| **Service** | `google_assistant.request_sync` | `google_assistant_secondary.request_sync` |
| **Storage** | `.storage/google_assistant` | `.storage/google_assistant_secondary` |

Both integrations share the same trait/device-type logic from the core `google_assistant` component — only the configuration, endpoint, entity filtering, and storage are independent.

## Prerequisites

- A working **primary** Google Assistant integration (the built-in one).
- A **second** Google Cloud project linked to the second Google account.

## Setup

### 1. Create a second Google Cloud project

Follow the [official HA Google Assistant manual setup guide](https://www.home-assistant.io/integrations/google_assistant/) but use the **second** Google account. You will get:

- A new `project_id`
- A new service account JSON (with `client_email` and `private_key`)

### 2. Set the fulfillment URL

In the Google Actions Console for the **second** project, set the fulfillment URL to:

```
https://YOUR_HA_URL/api/google_assistant_secondary
```

Note the `_secondary` suffix — this is what routes requests to this component instead of the primary one.

### 3. Install the custom component

Copy the `google_assistant_secondary` folder to your Home Assistant `custom_components/` directory:

```
config/
  custom_components/
    google_assistant_secondary/
      __init__.py
      button.py
      config_flow.py
      const.py
      http.py
      manifest.json
      strings.json
```

### 4. Configure in `configuration.yaml`

```yaml
# Primary integration (already configured)
google_assistant:
  project_id: my-primary-project-id
  service_account: !include service_account_primary.json
  report_state: true
  entity_config:
    light.living_room:
      expose: true
    light.bedroom:
      expose: false

# Secondary integration (this component)
google_assistant_secondary:
  project_id: my-secondary-project-id
  service_account: !include service_account_secondary.json
  report_state: true
  expose_by_default: false
  entity_config:
    light.bedroom:
      expose: true
      name: "Bedroom Light"
      room: "Bedroom"
    switch.desk_lamp:
      expose: true
```

### 5. Restart Home Assistant

After restarting, link the second Google account to the second project via the Google Home app. The second account will only see the entities exposed in the `google_assistant_secondary` configuration.

## Configuration options

Identical to the built-in `google_assistant` integration:

| Key | Required | Default | Description |
|---|---|---|---|
| `project_id` | yes | | Google Actions project ID |
| `service_account` | no | | Service account JSON (needed for `report_state` and `request_sync`) |
| `report_state` | no | `false` | Proactively report state changes to Google |
| `expose_by_default` | no | `true` | Expose all supported entities by default |
| `exposed_domains` | no | (all supported) | List of domains to expose by default |
| `entity_config` | no | | Per-entity overrides (expose, name, aliases, room) |
| `secure_devices_pin` | no | | PIN code for secure device actions |

## Tips

- Set `expose_by_default: false` on one or both integrations, then explicitly expose only the entities each account should control.
- Each integration has its own "Synchronize devices" button entity for triggering a manual sync.
- The `google_assistant_secondary.request_sync` service can be called from automations.

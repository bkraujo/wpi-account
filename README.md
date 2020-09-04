# wpi-account

This project is a general purpose Account Engine. It's main goal is to store named accounts with any arbitrary metadata.

The API object is a follows:

```json
{
  "name": "---",
  "kind": "---",
  "active": true,
  "labels": {
    "name": "value"
  }
}
```
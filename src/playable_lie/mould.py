"""Sprite mould loading and validation.

The first implementation belongs here. Keep the public surface small:

- load a JSON manifest
- validate it against schemas/mould.schema.json
- expose immutable frame and animation records
- verify every frame fits inside the declared canvas
- verify every animation references existing frame IDs
"""

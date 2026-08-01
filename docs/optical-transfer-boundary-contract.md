# Optical Transfer Boundary Contract

`SET` may describe screen-to-camera optical transfer as an offline transport
class for small payloads. It does not grant permission to import external code,
send secrets, or treat optical transfer as a reliable bulk transport.

This contract adapts the useful part of `bashalarmistalt/decimen-optical-transfer`:
fountain-coded animated QR frames for one-way, loss-tolerant file transfer
between a screen and a camera.

Source: https://github.com/bashalarmistalt/decimen-optical-transfer

## Allowed use

- small configuration payloads;
- diagnostic bundles;
- recovery packets;
- pairing tokens that are short-lived and non-secret or encrypted;
- signed command packets;
- firmware metadata;
- browser-readable troubleshooting export/import experiments.

## Transport states

- `planned`: payload shape and device direction are known.
- `encoded`: manifest, checksum, and chunks exist.
- `displaying`: sender is showing optical frames.
- `receiving`: receiver is decoding frames.
- `verified`: checksum/signature and manifest match.
- `rejected`: receiver rejected inconsistent, oversized, expired, or unsigned
  input.

## Payload manifest

Every optical payload should include:

- `payload_type`;
- `payload_version`;
- `total_len`;
- `max_total_len`;
- `chunk_size`;
- `chunk_count`;
- `checksum`;
- `expires_at` when useful;
- `sender_label`;
- `receiver_target`;
- `signature` when the payload can change device behavior.

## Required guardrails

- cap payload size before allocation;
- reject inconsistent `total_len`, chunk count, or manifest fields;
- reject unknown payload types;
- verify checksum before use;
- require signature for command-like payloads;
- time out stalled transfers;
- never persist decoded payloads automatically;
- never treat a visual QR stream as private.

## Project routing

| Project | Status | Boundary |
|---|---|---|
| `cardputer` | allowed_experiment | Mac/phone to device first, tiny payloads only |
| `CortexABV-private` | reference_only | offline evidence/package transfer idea only |
| `CoqPi` | reference_only | rare prep-packet handoff, no live-call dependency |
| public sites | not_useful | use normal web delivery |

## Acceptance rule

An optical-transfer pilot is accepted only after real hardware constraints are
known: camera availability, decode rate, display size, frame rate, maximum safe
payload size, and recovery behavior. Until then, it remains an experiment.

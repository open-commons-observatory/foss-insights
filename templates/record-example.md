---
kind: "issue"
id: 1836
title: "HTTPS probe reports available for a blocked site"
url: "https://github.com/OWNER/REPO/issues/1836"
date: "2025-10-27"
state: "closed/completed"
status: "analyzed"
depth: "full"
tagged_by: "manual"
classes: ["D3", "M1"]
tags: ["layer:probe", "cause:byte-cutoff", "conf:stated", "outcome:workaround"]
cited_in: ["analysis/10-measurement-validity.md"]
---

## Summary
The handshake succeeds and the stream stalls after about 16 KB, so a probe that checks only the connection or a short response reports the site as available; the maintainer says only crafted fakes help and testing must be manual.

## Notes

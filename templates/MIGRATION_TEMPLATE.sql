-- Migration: NNN_description
-- From schema: N-1
-- To schema: N
-- Data classification: cache | permanent
-- Backup required: yes | no

BEGIN IMMEDIATE;

-- CREATE/ALTER/COPY statements here.
-- Validate row counts before destructive steps.

PRAGMA user_version = N;

COMMIT;

#!/bin/bash

exec python cron_jobs.py &
exec python price_service_server.py
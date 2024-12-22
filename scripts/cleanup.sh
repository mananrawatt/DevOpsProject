# scripts/cleanup.sh
#!/bin/bash

# Variables
BACKUP_DIR="/var/backups"

# Clean up old backups (older than 7 days)
find ${BACKUP_DIR} -type d -mtime +7 -exec rm -rf {} +

echo "Cleanup completed."

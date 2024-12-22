# scripts/backup.sh
#!/bin/bash

# Variables
SOURCE_DIR="/var/lib/jenkins/workspace/your-pipeline-name"
BACKUP_DIR="/var/backups"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_PATH="${BACKUP_DIR}/backup_${TIMESTAMP}"

# Create backup
mkdir -p ${BACKUP_PATH}
cp -r ${SOURCE_DIR}/* ${BACKUP_PATH}

# Clean up old backups (older than 7 days)
find ${BACKUP_DIR} -type d -mtime +7 -exec rm -rf {} +

echo "Backup completed at ${BACKUP_PATH}"

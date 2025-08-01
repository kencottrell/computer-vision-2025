from datetime import datetime, timedelta

# e.g., delete images older than 30 days
cutoff_date = datetime.utcnow() - timedelta(days=30)
for image in images:
    if image.time_created < cutoff_date and not image.lifecycle_state == 'DELETED':
        compute.delete_image(image.id)
        print(f"Deleted image: {image.display_name}")

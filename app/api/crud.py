from sqlalchemy.orm import Session

import models
import schemas


def get_logs(db: Session):
    logs = db.query(models.Events).filter(models.Events.type_name == "user").all()
    return logs

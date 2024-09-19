import falcon
from models import Configuration
from db import get_session


class ConfigResource:
    def on_post(self, req, resp):
        session = get_session()
        
        data = req.media
        config = Configuration(
            instance_type=data['instance_type'],
            conditions=data['conditions'],
            actions=data['actions']
        )
        session.add(config)
        session.commit()
        resp.status = falcon.HTTP_201
        resp.media = {'message': 'Configuration added successfully'}

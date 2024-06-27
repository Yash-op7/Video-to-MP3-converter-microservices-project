import pika, json

def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)     # try to put the video file in mongo db using fs which is the gridfs object encapsulating mongo db object encapsulating the server object
    except Exception as err:
        return "internal server error, uploading video to mongodb failed", 500
    
    # if the code reaches here then file is sucessfully uploaded so now put a mesage on the queue
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"]
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE    # ! v important to ensure that our messages on the queue are persistent in nature in the event of a pod crash or restart, since our pod for our rabbit mq queue is a stateful pod withihn our k8s cluster  we need to ensure that when the messages are added to the quee they are persistent so that when the pod crashes and spins back up the messages are there when the pod is restored baack to its original state, so we make our queue durable which means the queue is retained when thepod restarts but we also need to make the messages on the queue to be durablek, so we just tell teh qeuue to persist the message until it is removed by us
            )
        )
    except:
        fs.delete(fid)  # if the message is failed to publish then we dont want there to be stale data in the mongo db when there is no message to process this data, so simply delete the data and ask the user to try again by returnign a internal serve rerror
        return "internal server error, failed to publish message, please try again", 500

        
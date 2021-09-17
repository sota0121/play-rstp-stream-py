import sys
import rtsp


def main(uri: str):
    with rtsp.Client(uri) as client:
        #_image = client.read()
        print(f'loading ... {uri}')
        client.read().show()
        

        ## Assertion fctx->async_lock failed at libavcodec/pthread_frame.c:167
        # while True:
        #     process_image(_image)
        #     _image = client.read(raw=True)


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('1 argument is required.')
        sys.exit(1)
    main(args[1])

import sys
import cv2


def main(uri: str):
    capture = cv2.VideoCapture(uri)

    while(True):
        ret, frame = capture.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('1 argument is required.')
        print('e.g.')
        print('python main.py rtsp://$USER:$PASS@IPADDRESS:port/xxx')
        sys.exit(1)
    main(args[1])

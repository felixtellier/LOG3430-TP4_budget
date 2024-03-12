import os
import sys


def main():
    if (os.system("python manage.py test") != 0):
        badCommit = os.popen("git rev-parse HEAD").read().strip()
        os.system(f"git bisect start {badCommit} e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
        firstBadCommit = os.popen("git bisect run python manage.py test").read().strip()
        os.system("git bisect reset")
        sys.exit(firstBadCommit)
    sys.exit(0)


if __name__ == '__main__':
    main()
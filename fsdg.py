import os, image, numpy, time


def create_image(width=1920, height=1080, num_of_images=100):
    width = int(width)
    height = int(height)
    num_of_images = int(num_of_images)

    current = time.strftime("%Y%m%d%H%M%S")
    os.mkdir(current)

    for n in range(num_of_images):
        filename = '{0}/{0}_{1:03d}.jpg'.format(current, n)
        rgb_array = numpy.random.rand(height, width, 3) * 255
        image = image.fromarray(rgb_array.astype('uint8')).convert('RGB')
        image.save(filename)


def main(args):
    create_image(width=args[0], height=args[1], num_of_images=args[2])
    return 0


if __name__ == '__main__':
    import sys

    status = main(sys.argv[1:])
    sys.exit(status)
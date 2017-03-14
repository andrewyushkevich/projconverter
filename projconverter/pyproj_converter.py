import argparse
import csv

from pyproj import Proj, transform


def argparser():
    parser = argparse.ArgumentParser(description="Convert coordiantes")
    parser.add_argument(
        "-p", "--path", help="Path to csv file with coordinates")
    parser.add_argument("-c", "--coordinates",
                        help="Reproject only one coordinate", nargs=3)
    parser.add_argument("-in", "--proj_in",
                        help="EPSG code of input projection")
    parser.add_argument("-out", "--proj_out", type=int,
                        help="EPSG code of output projection")

    return parser.parse_args()


def read_file(path):
    with open(path) as csvfile:
        rows = csv.DictReader(csvfile)
        coords = []
        for line in rows:
            coords.append((line))

    return coords


def convert_proj(proj_in, proj_out, path=None, coordinates=None):
    if path != None:
        coords = read_file(path)
        transform_coords = []
        for coord in coords:
            x, y, z = transform(proj_in, proj_out, 
                                coord['longitude'], coord['latitude'], coord['height'])
            transform_coords.append((x, y, z))
        print transform_coords

    elif coordinates != None:
        x, y, z = transform(proj_in, proj_out, 
                            coordinates[0], coordinates[1], coordinates[2])
        print x, y, z


def main():
    args = argparser()

    try:
        proj_in = Proj(init='epsg:' + str(args.proj_in))
        proj_out = Proj(init='epsg:' + str(args.proj_out))
        new_coords = convert_proj(proj_in, proj_out, 
                                  path=args.path, coordinates=args.coordinates)

    except RuntimeError:
        print "Wrong EPSG code"

if __name__ == '__main__':
    main()

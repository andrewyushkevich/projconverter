import argparse
import csv

from pyproj import Proj, transform


def argparser():
    parser = argparse.ArgumentParser(description="Convert coordiantes with pyproj")
    parser.add_argument("-p", "--path", 
                        help="Path to csv file with coordinates")
    parser.add_argument("-c", "--coordinate",
                        help="Reproject only one coordinate", nargs=3)
    parser.add_argument("-in", "--proj_in", type=int,
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


def convert_proj(proj_in, proj_out, path=None, coordinate=None):
    if path != None:
        data = read_file(path)
        new_coordinates = []
        for line in data:
            x, y, z = transform(proj_in, proj_out, 
                                line['longitude'], line['latitude'], line['height'])
            new_coordinates.append((x, y, z))
        print new_coordinates

    elif coordinate != None:
        new_coordinate = transform(proj_in, proj_out, 
                            coordinate[0], coordinate[1], coordinate[2])
        print new_coordinate


def main():
    args = argparser()

    try:
        proj_in = Proj(init='epsg:' + str(args.proj_in))
        proj_out = Proj(init='epsg:' + str(args.proj_out))
        new_coords = convert_proj(proj_in, proj_out, 
                                  path=args.path, coordinate=args.coordinate)

    except RuntimeError:
        print "Wrong EPSG code"

if __name__ == '__main__':
    main()

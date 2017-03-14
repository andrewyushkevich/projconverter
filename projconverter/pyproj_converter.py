import argparse
import csv
from pyproj import Proj, transform


def argparser():
    parser = argparse.ArgumentParser(description="Convert coordiantes")
    parser.add_argument("-p", "--path", 
    					help="Path to csv file with coordinates")
    parser.add_argument("-c", "--coordinates",
                        help="Reproject one coordinate", nargs=3)
    parser.add_argument("-in", "--proj_in", help="Default projection")
    parser.add_argument("-out", "--proj_out", type=int, help="Out projection")

    return parser.parse_args()


def read_file(path):
    with open(path) as csvfile:
        rows = csv.DictReader(csvfile)
        coords = []
        for line in rows:
            coords.append((line))

    return coords


def convert_proj(proj_in, proj_out, path):
    coords = read_file(path)
    transform_coords = []
    for coord in coords:
        print coord
        x, y, z = transform(proj_in, proj_out, coord['longitude'], coord[
                            'latitude'], coord['height'])
        transform_coords.append((x, y, z))

    return transform_coords


def main():
    args = argparser()
    proj_in = Proj(init='epsg:' + str(args.proj_in))
    proj_out = Proj(init='epsg:' + str(args.proj_out))
    transform_coords = convert_proj(proj_in, proj_out, args.path)

    print transform_coords

if __name__ == '__main__':
    main()

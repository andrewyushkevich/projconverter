# BSD 3-Clause License
# 
# Copyright (c) 2017, Andrew Yushkevich
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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

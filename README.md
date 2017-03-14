# Projconverter
A simple Python CLI tool to reproject coordinates.

## Dependencies

`pyproj`

## Installation

Clone and run `make install`

## Usage
```
projconverter [-h] [-p] [-c] [-in] [-out]

arguments:
  -h, --help            Show this help message and exit
  -p, --path            Path to csv file with coordinates
  -c, --coordinate      Reproject only one coordinate
  -in, --proj_in        EPSG code of input projection
  -out, --proj_out      EPSG code of output projection
```

### Arguments

* `path`
> Add path to your .csv file in ' '.    

> .csv file structure must be like in example:    
>`longitude,latitude,height`     
>`2762735.3759,1616618.9269,5498326.2280`    
>`2762735.3759,1616618.9269,5498326.2280`    
>`..., ..., ...`

* `coordinate`
> Add only one coordinate to reproject it.    
> Form of coordiantes must be (x, y, z) or (x.x, y.y, z.z) of latitude, longitude, height.

* `proj_in`
> Add EPSG code of input projection

* `proj_out`
> Add EPSG code of output projection

### Result

As a result you'll get list of tuples or tuple (if you reproject only one coordinate).

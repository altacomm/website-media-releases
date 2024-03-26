# website-media-releases

## Usage

* File names should start with a date in the format of `YYYYMMDD` to provide reverse-chronological ordering
* Files should have the extension `.md`
* Article titles should begin with a level 1 heading (i.e. `#`)
* Article descriptions should begin with a level 2 heading (i.e. `##`)
* `combine.py` will combine and parse the found `.md` files into a various files in the `./build/` directory

## Testing

To test this locally, run `http-server --cors` and `python combine.py`

## Example

See [EXAMPLE.md](articles/EXAMPLE.md)

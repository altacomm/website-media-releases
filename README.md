# website-media-releases

## Usage

* File names should start with a date in the format of `YYYYMMDD` to provide reverse-chronological ordering
* Files should have the extension `.md`
* Article titles should begin with a level 2 heading (i.e. `##`)
* `combine.py` will combine and parse the found `.md` files into a single `media-releases.html` with a horizontal rule inserted between each article

## Testing

To test this locally, run `http-server` and `python combine.py`

## Example

```md
## Title

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quis lacus ut risus aliquam vehicula. Duis sed tempor justo. Etiam hendrerit quis libero sed semper. Aenean ac diam lacus. Suspendisse consequat massa eget imperdiet lobortis. Vestibulum varius sem eu arcu maximus consectetur. Morbi congue tempor ligula, posuere auctor ipsum. Donec elementum justo a ipsum sagittis tempus. Quisque neque purus, fermentum eget magna faucibus, iaculis luctus nisl. Suspendisse molestie, risus id molestie egestas, augue tellus ultrices odio, vitae malesuada est ex et ex. Phasellus pretium, dolor eget scelerisque mollis, velit turpis ullamcorper turpis, non vulputate odio justo eu neque. Proin vitae sem est. Aenean id eros ipsum. Curabitur consectetur accumsan cursus. Nunc quis dolor nec ipsum aliquam vehicula non ac erat.

[Link](https://localhost/)

* Bullet point 1
* Bullet point 2

<!-- the python markdown parser inexplicably merges lists and wraps some bullet points in <p> when there are consecutive but clearly distinct lists in the absence of this comment (or other non-list elements), better solution to be researched -->

1. List item 1
2. List item 2
```

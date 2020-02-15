Appify
======

Easily wrap a regular binary into a macOS .app bundle.

Features:

* Takes care of bundling all .dylibs (recursively)
* Wrangles a PNG icon into an ICNS

NB: Only works on an actual Mac machine!

Usage
-----

E.g.

```
python -m appify \
	--executable ../paulstretch/bin/paulstretch \
	--bundle ./Paulstretch.app \
	--icon-png ../paulstretch/icon/icon.png
```

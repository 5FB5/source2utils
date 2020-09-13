***HEY! These utilities are still broken in a lot of ways and will fail very often. Please use with the understanding that it doesn't perfectly convert files yet and will only go through certain texture sets perfectly.***

# source2utils

This is a 3rd generation fork, first created by Rectus and then Forked by DankParrot/Alpyne and Caseytube. These are a set of scripts to help convert Source 1 assets to Source 2 with ease, partly using the tools Valve already have available, and using a materials script that takes a lot of guesswork. These tools were intended to be used with the Source 2 Filmmaker, but can be applied to any Source 2 project.

![screenie-1](https://i.imgur.com/XvADzGe.jpg)
![screenie-2](https://i.imgur.com/yYJu0fI.jpg)

Below is a list of branches that have been tested with the tool (with the HL:A Bootleg Tools):
- Source Filmmaker Branch (most content from this build is stable and should work nicely.)
- Half-Life: 2 (character models and some others crash while trying to compile, but then finish compiling fine)
- Counter-Strike: Source
- Black Mesa Source (same as HL2)
- Team Fortress 2 (Models compile fine, but HWM characters are pretty well broken)

Below is a list of branches that DON'T work with this tool (with the HL:A Bootleg Tools):
- Left 4 Dead 2 (most content works, but player models crash the engine.)
- Half-Life 1 (this should be obvious but just in-case you were curious)

## Installation Instructions
1. Go to the Releases Tab on the top right of this page

2. Download the latest release and extract to anywhere.

3. Download and set up the [Half-Life Alyx Bootleg Tools](https://github.com/thenayr/Half-Life-Alyx-SDK)

4. Run the scripts as instructed below.

## vmt_to_vmat.py

A more advanced script meant to help ease the conversion process of materials from Source 1's phong-specular approach to the modern PBR-specular approach in most Source 2 games.

**I would recommend to run this script first as it prepares your modname_imported folder, which will be where your imported content will live.**

To run, you will need to have all your materials in the content folder of your target game (for instance, steamapps/common/Half-Life Alyx/content/tf/materials), **with the .VTFs converted to .TGAs (best to do this with VTFEdit's "Tools->Convert Folder" process.)** Then, run the tool and point it in the direction of the "materials" folder or the specific .VMT you wish to convert. This will create a new content folder called "modname_imported" which will be where your imported content will live and be compiled out of.

Once that's done, open your tools and it will hang for a minute. I'd recommend listing "Materials" as the only asset type on the top right, going into "List" mode on the top left of the Asset Browser, and then selecting all of your materials by pressing "CTRL+A" and right clicking them, then clicking "Force Recompile." This will take a long time depending on your computer and how many materials you have, so set this up and walk away for a bit. After that's done, just right click and select "Refresh Thumbnails" and your content should be pretty easy to load from there.

## mdl_to_vmdl.py

Generates a .vmdl file that will tell Source 2 to import its accompanying .mdl file. You **must** leave the .mdl with the .vmdl file, or else it won't compile!

To run, you will need to have all your models in the content folder of your target game (for instance, steamapps/common/Half-Life Alyx/content/tf_imported/models). This should be the same folder as the path generated by the vmt_to_vmat tool. Then, run the tool and point it in the direction of the "models" folder or the specific .MDL you wish to convert.

You have two ways to convert your models - automatic and manual mode. If you select automatic mode (a), the program will read all paths you need from the "paths.txt " file that you must create in directory with program, after that converting will begin. 
![screenshot_automode_example](https://imgur.com/WG0sHpo.jpg)
Example of "paths.txt" file 
![screenshot_pathfile_example](https://imgur.com/dKucEjk.jpg)

In manual mode (m) , you can enter specific path individually an unlimited number of times.
![screenshot_manualmode_example](https://imgur.com/lhAO2H9.jpg)

Once that's done, open your tools and it will hang for a minute. I'd recommend listing "Models" as the only asset type on the top right, going into "List" mode on the top left of the Asset Browser, and then selecting all of your models by pressing "CTRL+A" and right clicking them, then clicking "Force Recompile." This will take a long time depending on your computer and how many materials you have, so set this up and walk away for a bit. After that's done, just right click and select "Refresh Thumbnails" and your content should be pretty easy to load from there.

## qc_to_vmdl.py

(deprecated)

An older attempt at converting models before I figured out how to directly import .mdl files.
You can use this as a base if you want to import the source files manually.

## Troubleshooting
##### *I got an error when converting materials! Something about not being able to convert something to something!*

If you get an error that says something like "ValueError: could not convert string to float," most likely your .VMT file has a parameter in it that is incorrectly formatted. Please refer to the [Valve Developer Community](https://developer.valvesoftware.com/wiki/Category:List_of_Shader_Parameters) for instructions on how your .VMTs should be formatted. Be sure to check for white space after the value, or white space inside of the quotation marks of the value. I also see a lot of `s (grave accents) where there should be quotes.

The plan is to stomp parsing errors like this out,

##### *My materials are appering as errors in the engine!*

There may be a couple non-uniform textures that don't parse correctly, and so the materials may show up as an error. To fix these, you must go to the material editor and find the problematic texture and correct it. Most likely, it will just be read as blank and 

##### *The material I'm trying to use is not compiling!*

Some materials, like sprites for particles, or cable materials for the old cable system, aren't converted over just yet. My main goal with this right now is to pass the VertexLitGeneric and LightmappedGeneric materials, with those other ones coming next.

In the interm, if you'd like to add an unsupported shader to the script, just download the original .py script and add your shaders into the "Supported Shaders" class on the top of the script. This will force them to pass through, but be warned that if your shader doesn't use $basetexture or any of the other standard .VMT parameters, it won't know what it's doing and will most likely compile incorrectly.

## System Requirements (for running the Python Scripts):
Python 3.7 or later
  * Libraries: tqdm, colorama, termcolor

[Python Image Library (PIL)  5.4.1](https://pillow.readthedocs.io/en/5.1.x/installation.html)

A Source 1 game's content, with the .vtfs extracted to .tgas in the same file structure as the .vmts

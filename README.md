# In-Jae-Font-Generator Preface

## Preface:

The high level idea of this side project was inspired by the application developed by In-Jae Company during the first hackathon in the K-Drama Start-Up (2020).
Therefore, all originality ideas are credited to the creators of Start-Up as I am simply just a fan trying to recreate the project practically to develop skills.
The general idea is the application takes in a human's handwriting (in the show they use handwriting from a bank's dataset),
either in the form of image input or drawing directly on a tablet, and by using AI, generate a series of fonts that companies could use for practical and/or commercial use. The fonts themselves are a reflection of the person's handwriting, but should not all characters be supplied, the AI model predicts what the rest of the remaining characters would look like.

### The benefits of this solution include:

- reducing the time and resources required for unique font generation
- supplementing a sample of characters to the entire set of Korean characters in that font (this repo focuses on English only)
- able to accept multiple input forms of sample characters

Based on the inspiration, my approach to this project is in a structured 2-stage development period:

### Stage 1: Building an Independent, OpenCV Pipeline that can simply take in handwriting and transform it into a .ttf file (font file)

- lower case letters only
- trains / develops on dataset handwriting (not user given)
- involves input preprocessing, glyph cleanup, vectorization, font assembly
- outputs .ttf file

### Stage 2: Apply ML Models to supplement characters not provided during input to create the .ttf file (more accurate to the Injae Idea)

- lower case / English only
- may use GANs, CNNs, etc
- aims to learn "style vector" for each writer

### Stage 3 (optional): Adding more scalable/product friendly features such as:

- adding punctuation, upper case letters, digits, other special characters
- multiple fonts created from one input (3/5?) with slight variations, but still resembles original input
- multi-language support

### More documentation will be updated here:

Stage 1 workflow process:

- input (from dataset) -> preprocessing.py -> segmentation.py -> vectorization.py -> font_builder.py -> font output (.ttf file)b

ben

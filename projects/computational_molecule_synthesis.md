---
layout: project-page
title: Computational Molecule Synthesis
excerpt: "Just about everything you'll need to style in the theme: headings, paragraphs, blockquotes, tables, code blocks, and more."
categories: [projects]
comments: false
---

### Project goal
The goal of this project was to develop open-source software which can decompose large molecules to small bio-active fragments, then use fragments to generate target molecules or new molecules for drug design.

### My role
Research Assistant

### My contribution

* Developed algorithms and open-source software (eMolFrag) to decompose large molecules to small bio-active fragments
* Tested the software on high performance computing (HPC) clusters and conducted benchmark test
* Wrote user's manual
* Generated libraries of fragments from the Directory of Useful Decoys, Enhanced (DUD-E) database, NuBBE database, Universal Natural Products database (UNPD), and ZINC database, respectively
* Optimized virtual screening search space
* Tested building targeted screening library with novel active compounds
* Maintained the software repository on GitHub and provided technical support

### Description of eMolFrag

eMolFrag is an open source software to decompose organic compounds into non-redundant sets of fragments retaining the connecticity information.

The code has been developed in Python. In order to perform the fragmentation process, eMolFrag utilizes BRICS algorithm implemented in the RDKit Python module.

Although the resulting fragments can be paired with a variety of virtual molecular synthesis tools, eMolFrag is specifically optimized to work with the software eSynth.


![I'm a relative reference to a repository file](../../Pics/computational_molecule_synthesis/Abstract.png)

Source code can be found at: [eMolFrag](https://github.com/liutairan/eMolFrag), [eSynth](https://github.com/liutairan/eSynth).    

eMolFrag is part of the [Deep Drug](https://www.deepdrug.org/) project, where the Deep Drug team was recognized as one of the top 10 teams in the [IBM Watson AI XPRIZE](https://www.xprize.org/articles/30-teams-advance-in-5m-ibm-watson-ai-xprize) competition.

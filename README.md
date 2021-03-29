# Dokumentacja do projektu benchmark proverów spass i prover9

## Dependencies

The following packages are requires

- pygmentize (python)
- minted (latex), depends on pygmentize
- texlive-core, texlive-science,

Optional

- plantuml-pdf - generating png, previewing, ex. `plantuml -tpng benchmark/domain_model.puml`


## Compile

Minted with custom lexers requires flag `-shell-escape`.
After generating glosaries latex must be recompiled to show properly. Mayby
there is better way, than showed below. Glossaries must be generated only once.

```sh
latexmk -output-directory="build" -aux-directory="build" -pdf -pv -shell-escape Documentation.tex
cd build
makeglossaries Documentation
cd ..
rm build/Documentation.pdf
latexmk -output-directory="build" -aux-directory="build" -pdf -pv -shell-escape Documentation.tex
```

Build dir is optional, clean with `latexmk -C`, or `rm -r build`

## Connected repos

- more tools: https://github.com/Mateusz-Grzelinski/sat-research


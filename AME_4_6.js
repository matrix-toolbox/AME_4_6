//
// MathJax 2.7.5
//
(function () {
    function mathjaxConfig() {
        MathJax.Hub.Config({"HTML-CSS": { preferredFont: "TeX", availableFonts: ["STIX","TeX"], linebreaks: { automatic:true }, EqnChunk: (MathJax.Hub.Browser.isMobile ? 10 : 50) },
            tex2jax: { inlineMath: [ ["$", "$"], ["\\\\(","\\\\)"] ], displayMath: [ ["$$","$$"], ["\\[", "\\]"] ], processEscapes: true, ignoreClass: "tex2jax_ignore|dno" },
            TeX: {
                extensions: ["begingroup.js"],
                noUndefined: { attributes: { mathcolor: "red", mathbackground: "#FFEEEE", mathsize: "90%" } },
                Macros: { href: "{}" }
            },
            displayAlign: "left",
            messageStyle: "none",
            styles: { ".MathJax_Display, .MathJax_Preview, .MathJax_Preview > *": { "background": "inherit" } },
            SEEditor: "mathjaxEditing"
        });
    }
    var config = document.createElement('script');
    config.type = 'text/x-mathjax-config';
    config.text = '(' + mathjaxConfig.toString() + ')();';
    document.head.appendChild(config);

    var loader = document.createElement('script');
    loader.src = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_HTML-full';
    document.head.appendChild(loader);
})();

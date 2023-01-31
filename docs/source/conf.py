# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'IMSE 440'
copyright = '2023, Fred Feng'
author = 'Fred Feng'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
# html_logo = "imse440-logo.png"
html_theme_options = {
    'display_version': False,
    'style_nav_header_background': '#00274C',
    # 'navigation_depth': 2,
    # 'titles_only': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_scaled_image_link = False

extensions = ['sphinx.ext.autosectionlabel',
            #   'sphinx_togglebutton',
              ]

# extensions = ['sphinx_tabs.tabs',
#               'sphinx.ext.autosectionlabel',
#               ]


html_title = ''
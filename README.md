# Rachel Herschmann's portfolio

The site lives in `site/`. It is plain HTML and CSS, with no build step.

## How changes go live

1. Make the change on a branch and open a pull request.
2. The **Preview** workflow checks the site and publishes a preview at
   `/pr-preview/pr-<number>/`. A bot comment on the pull request links to it.
   Previews are hidden from search engines.
3. Merge the pull request. The **Deploy site** workflow checks the site again
   and publishes it. The preview is removed.

GitHub Pages serves the `gh-pages` branch, which only the workflows write to.

`scripts/check_site.py site` runs the same check locally.

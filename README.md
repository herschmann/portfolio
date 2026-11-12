# Rachel Herschmann's portfolio

The site lives in `site/`. It is plain HTML and CSS, with no build step.
Cloudflare Pages publishes it to https://rachelherschmann.com.

## How changes go live

1. Make the change on a branch and open a pull request.
2. Cloudflare checks the site and builds a preview. Its link shows up on the
   pull request. Preview links are hidden from search engines.
3. Merge the pull request. Cloudflare checks the site again and publishes it
   to rachelherschmann.com.

If the check fails, nothing is published. `python3 scripts/check_site.py site`
runs the same check locally.

## Cloudflare Pages settings

- Production branch: `main`
- Build command: `python3 scripts/check_site.py site`
- Build output directory: `site`

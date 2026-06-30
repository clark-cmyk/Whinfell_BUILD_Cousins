# Desk Preview — Private GitHub Pages Access

**Status:** Repo is **private** · Pages **paused** until GitHub Pro is active  
**Owner:** Clark · **Reviewer:** Wes (invite after Pro upgrade)  
**Updated:** 2026-06-30

---

## What changed

| Before | After |
|--------|-------|
| Public repo | **Private** repo (`clark-cmyk/Whinfell_BUILD_Cousins`) |
| Public Pages — anyone with URL | **Private Pages** — GitHub login + repo read access only |
| `latest.json` world-readable | Same URL gated behind GitHub auth |

**Why Pages is offline right now:** GitHub Free does not support Pages on private repositories. The API returns:

> `Your current plan does not support GitHub Pages for this repository.`

Upgrade to **GitHub Pro** (~$4/month personal) to re-enable Pages with private visibility.

---

## Clark checklist (one-time)

### Step 1 — Upgrade to GitHub Pro

1. Open https://github.com/settings/billing/plans
2. Upgrade personal account to **GitHub Pro**
3. Confirm billing is active

### Step 2 — Re-enable private Pages

1. Repo → **Settings** → **Pages**
2. **Build and deployment** → Source: **GitHub Actions** (workflow: `Desk preview (GitHub Pages)`)
3. **GitHub Pages visibility** → **Private** (only people with repo access)
4. Save

### Step 3 — Trigger a deploy

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
bash scripts/publish_desk_preview.sh
```

Or: GitHub → **Actions** → **Desk preview (GitHub Pages)** → **Run workflow**

### Step 4 — Note the private Pages URL

After first successful deploy, Settings → Pages shows **Visit site**.  
Private sites may use a distinct Pages URL — **copy the URL from Settings**, not an old bookmark.

Legacy public URL (may 404 until re-deployed as private):

`https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/`

### Step 5 — Invite Wes

Wes needs a **GitHub account** and **Read** access to the repo.

**GitHub UI:**

1. Repo → **Settings** → **Collaborators** (or **Manage access**)
2. **Add people** → enter Wes's GitHub username
3. Role: **Read** (sufficient for private Pages viewing)

**Terminal (replace `WES_GITHUB_USERNAME`):**

```bash
gh api repos/clark-cmyk/Whinfell_BUILD_Cousins/collaborators/WES_GITHUB_USERNAME \
  -X PUT \
  -f permission=read
```

Wes accepts the email invite, signs in to GitHub, then opens the Pages URL.

---

## Wes instructions (send after invite)

1. Accept the GitHub collaborator invite (check email).
2. Sign in at https://github.com
3. Open the desk URL Clark sends (from repo **Settings → Pages**).
4. If prompted, authorize GitHub Pages access for the private site.
5. Hard-refresh: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows).

**No clone, no terminal, no import step** — Transmission Control auto-hydrates from co-hosted `latest.json` when signed in.

---

## Clark daily publish (unchanged)

After morning chain:

```bash
bash scripts/publish_desk_preview.sh
```

GitHub Actions redeploys in ~1–2 minutes. Only collaborators see the update.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Pages 404 / not found | Confirm GitHub Pro active · Settings → Pages → GitHub Actions source · run workflow |
| Wes sees 404 | Confirm invite accepted · signed into GitHub · using URL from Settings → Pages |
| `latest.json` still public | Repo must stay private · Pages visibility must be **Private** |
| Want to revert to public | `gh repo edit clark-cmyk/Whinfell_BUILD_Cousins --visibility public --accept-visibility-change-consequences` then set Pages visibility Public |

---

## Security notes

- Private Pages is **real** access control (GitHub auth + collaborator list).
- Do not commit secrets to the repo — hydration JSON is desk metrics, not credentials.
- Revoke access: remove collaborator in Settings → Collaborators.

---

*Option 1 locked: private repo + private Pages + invited reviewers.*
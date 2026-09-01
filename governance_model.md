# Governance model for updating the SI Reference Point

The knowledge model of the SI Reference Point (SIRP) is versioned according to the [Semantic Versioning scheme](https://semver.org/). To make updates to the SIRP, the following steps are proposed: 1. Reception and registration of a request 2. Assessment and prioritization 3.

Each step is further described below.

## 1. Reception and registration of a request

Requests can be made by anyone in the community via a GitHub issue, email, or verbal communication during meetings, among other ways. Some requests may respond to updates in reference documents (mainly the SI Brochure), may be reports of errors (bugs), or demands for new features.

Requests that are not received as a GitHub issue shall be registered as such in one of the public repositories. However, before opening a new issue, the issues of the public repositories are assessed for entries that already relate to the topic. If there is already an ongoing discussion, the new information is registered as a comment on behalf of the person who originally made the request. On the contrary, a new issue is registered on behalf of the person who originally made the request. In any case, the lin to the new issue or to the comment in the ongoing discussion shall be shared with the person who submitted the request.

> *CP: How do we decide which issues go to which repository? Maybe knowledge-model-related to the [generation scripts repo](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) and web-services-related to the [SI Digital Framework repo](https://github.com/TheBIPM/SI_Digital_Framework)? Issues can be moved between public repositories and original links will redirect to the new locations.*

> *CP: Do we request consent from the person to publish the issue (or the comment) on his/her behalf?*

All issues are automatically added to the backlog of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) (in GitHub, with restricted access).

## 2. Assessment and prioritization

This step occurs at the expert group meetings that are convened by the BIPM. Anyone, whether an expert group member or not, can comment on any issue at any time. The comments are useful to advance the discussion before the meeting. At every meeting, the participants assess the dashboard of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) that organizes the topics in different status fields. All issues start in status **Backlog**, meaning that it has been registered and may contain additional comments, but no decision has been made. The issues in backlog are discussed and may be assigned a new status depending on the consensus reached:

- **Planned**: The request is reasonable or necessary and will be advanced in due time.
- **Consultation**: The expert group participants consider that the topic must be discussed at a different instance: the SIDF task group, a working group of the CIPM Forum on Metrology and Digitalization (FORUM-MD), the Consultative Committee of Units (CCU), or another Consultative Committee of the CIPM.
- **Done**: The request tackles a topic that has already been solved or is a duplicate of another issue.
- **Not planned**: The request has been deemed unsuitable under current circumstances.

Before moving the status of any issue in the backlog, a comment is added with a summary of the discussion held and the conclusion reached. In case the status is set to **Done** or **Not planned**, the issue is closed.

For issues moved to **Consultation**, the participants must agree on the instance to which the topic will be taken and a responsible person must be defined. At the next meeting, a follow-up of issues under consultation is made. Afterward, the issue may be moved to **Not planned** or to **Planned**.

For issues with status **Planned**, a prioritization level must be assigned by adding one of the issue tags `planned-high-priority`, `planned-medium-priority,` and `planned-low-priority`. Furthermore, the impact of implementing the solution to the issue is estimated, according to the instances adapted from the [Semantic Versioning scheme](https://semver.org/): \* Major version updates when the changes will introduce incompatibility with former versions of the knowledge model (e.g. eliminating a class, renaming a datatype property) \* Minor version updates when a feature will be introduced in a backward compatible manner (e.g. adding new individuals, like new units of measurement) \* Patch updates when a bug you make backward compatible bug fixes (e.g. fixing a comment o relabeling an individual)

Changes that will reflect on major version updates are discussed and approved at the Task Group level, while the changes that will reflect on a patch or minor version updates are discussed and approved at the expert group level (see Section \##).

One or more expert group members may volunteer to work on the implementation. This assignment is declared on the webpage of the issue.

## 3. Branch creation and code development

The repository will always hold two permanent branches: \* Branch `origin/main`, which will always reflect the last stable release of the knowledge model available in the [SI Digital Framework website](https://si-digital-framework.org/) and in the [SI Digital Framework repository](https://github.com/TheBIPM/SI_Digital_Framework). \* Branch `origin/develop`, which contains the last feature implementations and bug fixes for the next release.

Additional feature/fix branches are created with a limited lifetime to start working on an issue with status **Planned**. These branches are created from branch `origin/develop` and should be named in an informative way, always including the number of the issue (e.g. `95-new-version-of-the-9th-edition-of-the-si-brochure-v4_01`, to work on [issue #95](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts/issues/95)). Then, the status of the issue is changed to **In progress** on the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6).

> *CP: If we adopt the issue number inclusion in the naming convention, then it could make sense to move knowledge-base-related issues to the scripts generation repository.*

Code patches are committed to the respective branch by the expert group members who volunteered on the work. People from the community can also contribute to the code writing under the steering of an expert group member. Commit messages should be informative but short. The issue can be referenced in commit messages by including the issue number after a hash sign. This action will add a note to the webpage of the issue.

The status of the implementations is updated at the expert group meetings by the group of people working on them. When a code patch is considered finished, the feature/fix branch should merge all the changes done in branch `origin/develop` (*CP: or to rebase?*), All merging conflicts must be solved before creating a pull request; then the status of the issue is changed to **In review** at the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6).

## 4. Expert group review

Issues with status **In review** are discussed at the expert group meetings. The review shall include testing the new knowledge model in the preproduction server of the web services of the SI Digital Framework (only available within the BIPM intranet and to external whitelisted IP addresses).

If the expert group members reach a consensus that an implementation is suitable and complete, the changes are merged into branch `origin/develop,` and the feature/fix branch is deleted. A comment is added to the webpage of the issue and its status is changed to **Awaiting release** on the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6). The summary of the implementations is updated in the release notes of the repository.

## 5. Approval and release

Patch or minor updates are approved at the discretion of the expert group. The SIDF-TG members are updated on the changes awaiting release. Major updates require approval of the SIDF-TG, who may decide to consult the changes with other working groups of the FORUM-MD, the CCU, or other Consultative Committees of the CIPM.

The approval of an update triggers the following actions:

1.  A version number is assigned.
2.  The knowledge model graphs are generated.
3.  The changes in branch `origin/develop` are merged into `origin/main`.
4.  The release is done in the [generation scripts repository](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) from the `origin/main` branch.
5.  The turtle files are updated in the [SI Digital Framework repository](https://github.com/TheBIPM/SI_Digital_Framework).
6.  The [SI Digital Framework website](https://si-digital-framework.org/) is restarted with the new knowledge model graphs.

Previous versions of the knowledge model should remain accessible by using the version URIs, but the canonical URLs should resolve to the last released version of the knowledge model.

The people who initially made requests that were satisfied in the last release are notified.

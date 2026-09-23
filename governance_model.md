# Governance model for updating the SI Reference Point

The SI Reference Point (SIRP) is a machine-actionable knowledge model of the SI Brochure [[#]]() developed by the expert group members of the (FORUM-MD Task Group on SI-digital Framework [FORUM-MD-TG-SIDF](https://www.bipm.org/en/committees/fo/forum-md/wg/forum-md-tg-sidf)).
The web services available at https://si-digital-framework.org/SI provide access to the knowledge model of the SIRP, and are developed by the BIPM.

The SIRP is versioned according to the [Semantic Versioning scheme](https://semver.org/), using three dot-separated integer numbers known as the major, minor and patch version.
The version control is handled at two public GitHub repositories that serve different purposes:

- [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts): A Python package that generates the knowledge graph of the SIRP serialized as Turtle and JSON-LD files.
- [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework): A read-only repository to track changes in the Turtle-serialized files of the SIRP and other ontologies.

Changes to the SIRP and the associated web services respond to feedback received from the user community.
The following steps are proposed for handling this feedback:

1.  Reception and registration of a request
2.  Classification, assessment and prioritization
3.  Code development
4.  Code review
5.  Approval and release

Each step is further described below.

## 1. Reception and registration of a request

Requests can be raised via GitHub issues, email, or verbal communication during meetings, among other ways.
Some requests may respond to updates in reference documents (mainly the SI Brochure), may be reports of errors in the knowledge base (bugs) or demands for new features. 

Requests that are not received as a GitHub issue shall be registered as such in either of the public repositories.
In this case, the person is invited to use their GitHub account, but if this is not feasible, someone else can register the reuest on their behalf.
Before opening a new issue, it is desirable to look for an already opened issue that that already relates to the topic.
In case there is already a related issue, the new information is added to the ongoing discussion as a comment.
On the contrary, a new issue is registered.
All requests must be submitted by an identifiable user, either in an individual capacity or on behalf of a body (e.g. working group of a CIPM Consultative Committee).
If the request was registered on behalf of someone else, a disclaimer shall be included (*On behalf of...*), and the link to the new issue (or to the comment) shall be shared with the person who originally submitted the request.

All issues filed in the two repositories are automatically added to the backlog of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) (accessible only to logged-in members of the Expert Group).


## 2. Classification, assessment and prioritization

> *include web-services-related and git-repository-related tags that are BIPM*
> JLH> Use labels, include i.e. *request from CC*, to identify the kind of issue. Support by CP. 
This step occurs at the expert group meetings that are convened by the BIPM. Anyone, whether an expert group member or not, can comment on any issue at any time. The comments are useful to advance the discussion before the meeting. At every meeting, the participants assess the dashboard of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) that organizes the topics in different status fields. All issues start in status **Backlog**, meaning that it has been registered and may contain additional comments, but no decision has been made. The issues in backlog are discussed and may be assigned a new status depending on the consensus reached:

- **Planned**: The request is reasonable or necessary and will be advanced in due time. Tag `planned`.
- **Consultation**: The expert group participants consider that the topic must be discussed at a different instance: the SIDF task group, a working group of the CIPM Forum on Metrology and Digitalization (FORUM-MD), the Consultative Committee of Units (CCU), or another Consultative Committee of the CIPM. In case of strong disagreement regarding a decision, the issue is moved to this status. The decision about which body to consult should be at least informed to the TG-SIDF. Tag `consultation`.
- **Done**: The request tackles a topic that has already been solved or is a duplicate of another issue. Tag `done`.
- **Not planned**: The request has been deemed unsuitable under current circumstances. Tag `not-planned`.

> JM: how is the agreement reached? democracy?
> GD: are we the rigth group? If the CC say X, 
> FM: We have better knowlegde of the feasible things to our knowledge graph.
> 

Before moving the status of any issue in the backlog, a comment is added with a summary of the discussion held and the conclusion reached. In case the status is set to **Done** or **Not planned**, the issue is closed.

For issues moved to **Consultation**, the members of the expert group of the TG SIDF present in the meeting must agree on the instance to which the topic will be taken and a responsible person must be defined. At the next meeting, a follow-up of issues under consultation is made. Afterward, the issue may be moved to **Not planned** or to **Planned**.

For issues with status **Planned**, a prioritization level must be assigned by adding one of the issue tags `high-priority`, `medium-priority,` and `low-priority`. Furthermore, the impact of implementing the solution to the issue is estimated, according to the instances adapted from the [Semantic Versioning scheme](https://semver.org/):
> MG: do not couple startus with priority.

- **Major** version updates when the changes will introduce incompatibility with former versions of the knowledge model (e.g. eliminating a class, renaming a datatype property).
- **Minor** version updates when a feature will be introduced in a backward compatible manner (e.g. adding new individuals, like new units of measurement).
- **Patch** updates when a bug you make backward compatible bug fixes (e.g. fixing a comment o relabeling an individual).

Changes that will reflect on major version updates are discussed and approved at the Task Group level, while the changes that will reflect on a patch or minor version updates are discussed and approved at the expert group level (see Section \##).

Major updates changes should not be merger to develop before discussing them to at the TG/level.

One or more expert group members may volunteer to work on the implementation. This assignment is declared on the webpage of the issue.

## 3. Code development

The repository will always hold two permanent branches: 

* Branch `origin/main`, which will always reflect the last stable release of the knowledge model available in the [SI Digital Framework website](https://si-digital-framework.org/) and in the [SI Digital Framework repository](https://github.com/TheBIPM/SI_Digital_Framework).
* Branch `origin/develop`, which contains the last feature implementations and bug fixes for the next release.

Additional feature/fix branches are created with a limited lifetime to start working on an issue with status **Planned**. These branches are created from branch `origin/develop` and should be named in an informative way, always including the number of the issue (e.g. `95-new-version-of-the-9th-edition-of-the-si-brochure-v4_01`, to work on [issue #95](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts/issues/95)). Then, the status of the issue is changed to **In progress** on the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6).

> *CP: If we adopt the issue number inclusion in the naming convention, then it could make sense to move knowledge-base-related issues to the scripts generation repository.*

Code patches are committed to the respective branch by the expert group members who volunteered on the work. People from the community can also contribute to the code writing under the steering of an expert group member. Commit messages should be informative but short. The issue can be referenced in commit messages by including the issue number after a hash sign. This action will add a note to the webpage of the issue.

The status of the implementations is updated at the expert group meetings by the group of people working on them. 

## 4. Code review

Issues with status **In review** are discussed at the expert group meetings. The review can include testing the new knowledge model in the preproduction server of the web services of the SI Digital Framework (only available within the BIPM intranet and to external whitelisted IP addresses).

**Rephrase**
When a code patch is considered finished, the feature/fix branch should merge all the changes done in branch `origin/develop` (*CP: or to rebase?*), All merging conflicts must be solved before creating a pull request; then the status of the issue is changed to **In review** at the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6).

> We do not need to all meet for small changes. BIPM Staff can decide merge requests to develop branches, CP: notify other expert group members, add a window for comments on one week, AS: supports. DC: no answers will mean everybody agrees?
> 
> 

If the expert group members reach a consensus that an implementation is suitable and complete, the changes are merged into branch `origin/develop,` and the feature/fix branch is deleted. A comment is added to the webpage of the issue and its status is changed to **Awaiting release** on the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6). The summary of the implementations is updated in the release notes of the repository.


## 5. Approval and release

Patch or minor updates are approved at the discretion of the expert group. The SIDF-TG members are updated on the changes awaiting release by email. *MG: Changes can be informed by email, the timeframe of the release in one week; FM: Objects to the notification; DC&JM no answers will mean everybody agrees. FM: why not using GitHub automatic notification system, GD supports, CP&AS GitHub sends to many of too few notifications, not too reliable.*

Major updates require approval of the SIDF-TG, who may decide to consult the changes with other working groups of the FORUM-MD, the CCU, or other Consultative Committees of the CIPM.

The approval of an update triggers the following actions:

1.  A version number is decided.
2.  The knowledge model graphs are generated.
3.  The changes in branch `origin/develop` are merged into `origin/main`.
4.  The release is done in the [generation scripts repository](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) from the `origin/main` branch.
5.  The turtle files are updated in the [SI Digital Framework repository](https://github.com/TheBIPM/SI_Digital_Framework).
6.  The [SI Digital Framework website](https://si-digital-framework.org/) is restarted with the new knowledge model graphs.

Previous versions of the knowledge model should remain accessible by using the version URIs, but the canonical URLs should resolve to the last released version of the knowledge model.

The people who initially made requests that were satisfied in the last release are notified.

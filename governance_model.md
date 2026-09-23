# Governance model for updating the SI Reference Point

The SI Reference Point (SIRP) is a machine-actionable knowledge model of the SI Brochure [[#]]() developed by the Expert Group members of the (FORUM-MD Task Group on SI-digital Framework [FORUM-MD-TG-SIDF](https://www.bipm.org/en/committees/fo/forum-md/wg/forum-md-tg-sidf)).
The web services available at https://si-digital-framework.org/SI provide access to the knowledge model of the SIRP, and are developed by the BIPM.

The SIRP is versioned according to the [Semantic Versioning scheme](https://semver.org/), using three dot-separated integer numbers known as the major, minor and patch version (see [Section Planned](#Planned)).
The version control is handled at two public GitHub repositories that serve different purposes:

- [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts):
A Python package that generates the knowledge graph of the SIRP serialized as Turtle and JSON-LD files.
- [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework):
A read-only repository to track changes in the Turtle-serialized files of the SIRP and other ontologies.

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
If the request was registered on behalf of someone else, a disclaimer shall be included (*On behalf of...*).
The link to the new issue (or to the comment) shall be shared with the person who originally submitted the request.

## 2. Classification, assessment and prioritization
All issues registered in the two repositories shall be added to the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) (accessible only to logged-in members of the Expert Group).

Upon registration, the issues are classified according to the scope (mandatory) and the requesting body (optional).
Suitable labels (`<label>`) shall be assigned to help identify, filter and prioritize them.

- Scope: Most issues are related to the ontology (label `ontology`) or to the web services (label `web-services`).
To a lesser extent, issues can be related to the management of the repository (label `repo-management`).
- Requesting body: Issues can be raised by representatives of the digitalization working group of a CIPM Consultative Committee (label `request-from-CC`), of a FORUM-MD working group (label `request-from-FORUM-MD`), or of a liaison organization (label `request-from-liaison-org`).
This information can help in the prioritazion of the topics.

> **Note:** The remaining part of this governance document applies to the issues related to the ontology of the SIRP.
The issues related to the web services or to the management of the repository are handled exclusively by the BIPM.

The Expert Group members gather at meetings convened by the BIPM to assess and prioritize the issues.
At every meeting, the issues in the dashboard of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) are discussed and reorganized in status boxes accordingly:

#### Backlog
All issues start here, meaning that have been registered and may contain additional comments, but no decision has been made.
The issues registered in the repository [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) are added automatically to the backlog, while those registered in the repository [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework) must be imported manually. Optionally, issues from other private repositotories (e.g. related to the web services) can be added here for easing the follow up of topics.

Before moving any issue from this box, a comment is added with a summary of the conclusion reached. The issues here can be moved to status <ins>Planned</ins>, <ins>Consultation</ins>, <ins>Done</ins> or <ins>Not planned</ins>.

#### Planned
Status for requests from the <ins>Backlog</ins> that have been considered feasible, reasonable or necessary and will be advanced in due time. This status is also possible for issues that were in <ins>Consultation</ins> (see below) afted feedback was collected and analyzed.

The label `status-planned` is assigned to the issues in this box. A priority level must be defined and indicated by adding one of the labels `high-priority`, `medium-priority,` or `low-priority`. Furthermore, the impact of implementing the solution to the issue shall be estimated, according to the following instances adapted from the [Semantic Versioning scheme](https://semver.org/):

- <ins>Major version updates</ins> when a change will introduce incompatibility with former versions of the knowledge model (e.g. eliminating a class, renaming a datatype property).
- <ins>Minor version updates</ins> when a feature will be introduced in a backward compatible manner (e.g. adding new individuals, like new units of measurement).
- <ins>Patch version updates</ins> when a bug will be fixed in a backward compatible manner (e.g. fixing a comment o relabeling an individual).

Changes that will reflect on major version updates must be discussed and approved at the Task Group level.

Depending on the prioritazion and complexity level of the issue, one or more Expert Group members may volunteer to work on the code implementation. This assignment is declared on the webpage of the issue. When the code implementation is ready to begin, the issue is moved to status <ins>In progress</ins>.

#### Consultation
Status for requests from the <ins>Backlog</ins> that must be discussed at a different instance because it implies a high metrological level decision or because there is strong disagreement among the Expert Group members regarding the suitability of an issue in the backlog.

The default instance to consider is the TG-SIDF meetings, but it can also be agreed to discuss the topic with another working group of the FORUM-MD, the Consultative Committee of Units (CCU), or another Consultative Committee of the CIPM.
At least one person must be designated as responsible for doing the consultation and the information gathered must be added as a comment to the issue webpage.
After the Expert Group members discuss the new information, the issue can be moved to status <ins> Planned </ins> or <ins> Not planned </ins>.

#### In progress
A planned issue

When the code implementation is considered finished, the issue is moved to status <ins>In review</ins>.

#### In review
A planned issue

#### Awaiting release
A planned issue

#### Done
The request tackles a topic that has already been solved or is a duplicate of another issue. Tag `done`. The issues is 

Issues moved to this status box are automatially closed as completed.

#### Not planned
The request has been deemed unsuitable under current circumstances. Tag `not-planned`.

Issues moved to this status box must be closed either as not planed or as duplicate, accordingly.

For other cases, the status of the issue is informed in the issue webpage by adding one of the labels, `status-in-consultation`, `status-in-progress`, `status-in-review`, `status-awaiting-release`.
For the issues 


> JM: how is the agreement reached? democracy?
> GD: are we the rigth group? If the CC say X, 
> FM: We have better knowlegde of the feasible things to our knowledge graph.
> 



## 3. Code development

The repository will always hold two permanent branches: 

* Branch `origin/main`, which will always reflect the last stable release of the knowledge model available in the [SI Digital Framework website](https://si-digital-framework.org/) and in the [SI Digital Framework repository](https://github.com/TheBIPM/SI_Digital_Framework).
* Branch `origin/develop`, which contains the last feature implementations and bug fixes for the next release.

Additional feature/fix branches are created with a limited lifetime to start working on an issue with status **Planned**. These branches are created from branch `origin/develop` and should be named in an informative way, always including the number of the issue (e.g. `95-new-version-of-the-9th-edition-of-the-si-brochure-v4_01`, to work on [issue #95](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts/issues/95)). Then, the status of the issue is changed to **In progress** on the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6).

> *CP: If we adopt the issue number inclusion in the naming convention, then it could make sense to move knowledge-base-related issues to the scripts generation repository.*

Major updates changes should not be merger to develop before discussing them to at the TG/level.

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

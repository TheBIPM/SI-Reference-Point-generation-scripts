# Governance model for updating the SI Reference Point
The SI Reference Point (SIRP) is a machine-actionable knowledge model of the SI Brochure [[#]]() developed by the Expert Group members of the [FORUM-MD Task Group on SI-digital Framework (FORUM-MD-TG-SIDF)](https://www.bipm.org/en/committees/fo/forum-md/wg/forum-md-tg-sidf).
The web services available at https://si-digital-framework.org/SI provide access to the knowledge model of the SIRP, and are developed by the BIPM.

The SIRP is versioned according to the [Semantic Versioning scheme](https://semver.org/), using three dot-separated integer numbers known as the major, minor and patch version (see [below](#Planned)).
The version control is handled at two public GitHub repositories that serve different purposes:

- [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts):
    A Python package that generates the knowledge graph of the SIRP serialized as Turtle and JSON-LD files.
- [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework):
    A read-only repository to track changes in the Turtle-serialized files of the SIRP and other ontologies.

Changes to the SIRP and the associated web services respond to feedback received from the user community.
The following steps are proposed for handling this feedback:

1.  Reception and registration of a request
2.  Classification, assessment and prioritization
3.  Development
4.  Review and approval
5.  Release

Each step is further described in this document.

<a name="note1"></a>
> **Note:**
    The procedures stated in this governance document apply to requests related to the SIRP (the knowledge model).
    Issues related to the web services or to the management of the repository are handled by the BIPM staff, who may nonetheless choose to apply some of these procedures at their own discretion.

## 1. Reception and registration of a request
Requests can be raised via GitHub issues, email, or verbal communication (e.g. during meetings), among other ways.
Some requests may respond to updates in reference documents (mainly the SI Brochure), may be reports of errors in the knowledge base (bugs) or demands for new features. 
All requests must be submitted by an identifiable user, either in an individual capacity or on behalf of a body (e.g. working group of a CIPM Consultative Committee).

Requests that are not received as a GitHub issue shall be registered as such in either of the two public repositories.
Before opening a new issue, it is desirable to look for an already opened issue that that already relates to the topic.
In case there is already a related issue, the new information should be added to the ongoing discussion as a comment.
On the contrary, a new issue is registered.
For these purposes, the person raising the issue can be invited to use their GitHub account, but if this is not feasible, the person receiving the request can file the issue on their behalf.
In this case, a disclaimer shall be included (*On behalf of...*), and the link to the new issue (or to the comment) shall be shared with the person who originally submitted the request.

## 2. Classification, assessment and prioritization
All registered requests are managed in the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) (accessible only to logged-in members of the Expert Group), wich provides a dashboard to follow up on the status of the requests.
Issues are assigned suitable labels (`<label>`) to help identify, filter and prioritize.

Upon registration, the issues are classified according to the scope (mandatory) and the requesting body (optional).

- Scope:
    Most issues are requests related to the ontology (label `ontology`) or to the web services (label `web-services`).
    To a lesser extent, issues can be related to the management of the repository (label `repo-management`).
    Some GitHub issues can be questions that do not demand changes (label `question`).
    These issues can be closed after the question has been addressed.
- Requesting body:
    Issues can be raised by representatives of the digitalization working group of a CIPM Consultative Committee (label `request-from-CC`), of a FORUM-MD working group (label `request-from-FORUM-MD`), or of a liaison organization (label `request-from-liaison-org`).
    This information can help in the prioritazion of the topics.

The Expert Group members gather at meetings convened by the BIPM to assess and prioritize the issues related to the knowledge model (see the [note](#note1) above).
At every meeting, the issues in the dashboard of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) are discussed and reorganized in status boxes:
[<ins>Backlog</ins>](#backlog), [<ins>Planned</ins>](#planned), [<ins>Consultation</ins>](#consultation), [<ins>In progress</ins>](#in-progress), [<ins>In review</ins>](#in-review), [<ins>Awaiting release</ins>](#awaiting-release), [<ins>Done</ins>](#done) or [<ins>Not planned</ins>](#not-planned).
The meaning of each status is described below.

<div style="padding-left: 50px; padding-right: 50px;" markdown="1">

---
#### Backlog
All issues start here, meaning that have been registered and may contain additional comments, but no decision has been made.
The issues registered in the repository [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) are added automatically to the backlog, while those registered in the repository [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework) must be imported manually.
Optionally, issues from other private repositories (e.g. related to the web services) can be added here for easing the follow up of topics.

The issues here are discussed during the meetings of the Expert Group and may thereafter be assigned the status [<ins>Planned</ins>](#planned), [<ins>Consultation</ins>](#consultation), or [<ins>Not planned</ins>](#not-planned), depending on the conclusion from themembers.
Before moving any issue from this box, a comment is added with a summary of the outcomes of the discussion.

---
#### Planned
This status is assigned to requests from the [<ins>Backlog</ins>](#backlog) that have been considered feasible, reasonable or necessary by the Expert Group members.
This status may also be assigned for request in [<ins>Consultation</ins>](#consultation) depending on the feedback that was collected from the higher instance.
Issues here are assigned the label `status-planned`, meaning that the Expert Group members undertake to advance them in due time.

A priority level must be defined by Expert Group members upon discussion.
The conclussion is made explicit by adding one of the labels `high-priority`, `medium-priority,` or `low-priority`.
Furthermore, the impact of implementing the solution to the issue shall be estimated, according to the following instances adapted from the [Semantic Versioning scheme](https://semver.org/):

- <ins>Major version updates</ins> when a change will introduce incompatibility with former versions of the knowledge model (e.g. eliminating a class, renaming a datatype property).
- <ins>Minor version updates</ins> when a feature will be introduced in a backward compatible manner (e.g. adding new individuals, like new units of measurement).
- <ins>Patch version updates</ins> when a bug will be fixed in a backward compatible manner (e.g. fixing a comment o relabeling an individual).

Changes that will reflect on major version updates must be discussed and approved at the TG-SIDF, which migth decide to further discuss the implications with other groups of the FORUM-MD or a CIPM Consultative Committee.

Depending on the prioritazion and complexity level of the issue, one or more Expert Group members may volunteer to work on the code implementation.
This volunteering is declared on the webpage of the issue using the GitHub function *Assignees*.
When the code implementation is ready to begin, the issue is assigned the status [<ins>In progress</ins>](#in-progress).

---
#### Consultation
This status is assigned to requests from the [<ins>Backlog</ins>](#backlog) that must be discussed at an instance higher than the Expert Group because it implies a high metrological level decision, or because there is strong disagreement among the Expert Group members regarding the suitability of the request.
Issues here are assigned the label `status-consultation`, meaning that the Expert Group members undertake to discuss the issue externally to make a decision.

The default instance to consider for consultation is the TG-SIDF, but the Expert Group members can also decide to discuss the topic dicrectly with another working group of the FORUM-MD, the Consultative Committee of Units (CCU), or another Consultative Committee of the CIPM.
At least one Expert Group member must be designated as responsible for doing the consultation.
When the information has been gathered, a summary must be added as a comment to the issue webpage.
After the Expert Group members discuss the newly collected information, the issue can be assigned the status [<ins>Planned</ins>](#planned) or [<ins>Not planned</ins>](#not-planned).

---
#### In progress
This status is assigned for issues marked [<ins>Planned</ins>](#planned) once some Expert Group members start working on the code implementation to address them.
Issues here are assigned the label `status-in-progress`, meaning that the request is being advanced. 

The details of this stage are given in Section [3. Development](#3-development).
When the code implementation is considered finished, the issue is assigned the status [<ins>In review</ins>](#in-review).

---
#### In review
This status is assigned to issues marked [<ins>In progress</ins>](#in-progress) once the people working on a request consider that the code implementation is complete.
Issues here are assigned the label `status-in-review`, meaning that a solution to a request has been proposed and it is being evaluated either by the Expert Group or at a higher instance.

The details of this stage are given in Section [4. Review and approval](#4-review-and-approval).
Depending on the outcome of the review, the issue can moved back to status [<ins>In progress</ins>](#in-progress), or advanced to status [<ins>Awaiting release</ins>](#awaiting-release).

---
#### Awaiting release
This status is assigned to issues marked [<ins>In review</ins>](#in-review), after the designated instance has approved the changes.
Issues here are assigned the label `status-awaiting-release`, meaning that the request was addressed and the changes will be published in the next release of the SIRP.

The details of this stage are given in Section [5. Release](#5-release).
After the release has been done, the issue is advanced to the last status [<ins>Done</ins>](#done).

---
#### Done
This status is achieved for issues that were marked [<ins>Awaiting release</ins>](#awaiting-release), after the updated knowledge model of the SIRP has been released.
The issues moved to this status box can be closed as completed.

---
#### Not planned
This status is assigned for issues from the boxes [<ins>Backlog</ins>](#backlog) or [<ins>Consultation</ins>](#consultation), when the corresponding decision body have considered them unsuitable under current circumstances.
The issues here are assigned the label `status-not-planned` and must be closed as such in the issue webpage.

---
</div>

> JM: how is the agreement reached? democracy?
> GD: are we the rigth group? If the CC say X, 
> FM: We have better knowlegde of the feasible things to our knowledge graph.
> 

## 3. Development
The development is done in the repository [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts).
This section describes the guidelines for branching and merging.

The repository will always hold two permanent branches: 

* Branch `origin/main`:
    Always reflect the version of the Python package that generates the last stable release of the SIRP, available both in the [website of the SI Digital Framework](https://si-digital-framework.org/) and in the [read-only repository of the SI Digital Framework](https://github.com/TheBIPM/SI_Digital_Framework).
* Branch `origin/develop`:
    Contains the last feature implementations and bug fixes that have been aproved for the next release of the SIRP.

Branches with a limited lifetime (feature/fix branches) are created when starting to work on an issue that was [<ins>Planned</ins>](#planned).
The feature/fix branches are created from the branch `origin/develop` and should be named in an informative way, always including the number of the issue (e.g. `95-new-version-of-the-9th-edition-of-the-si-brochure-v4_01`, to work on [issue #95](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts/issues/95)). Then, the status of the issue is changed to **In progress** on the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6).

> *CP: If we adopt the issue number inclusion in the naming convention, then it could make sense to move knowledge-base-related issues to the scripts generation repository.*

Major updates changes should not be merger to develop before discussing them to at the TG/level.

Code patches are committed to the respective branch by the expert group members who volunteered on the work. People from the community can also contribute to the code writing under the steering of an expert group member. Commit messages should be informative but short. The issue can be referenced in commit messages by including the issue number after a hash sign. This action will add a note to the webpage of the issue.

The status of the implementations is updated at the expert group meetings by the group of people working on them. 

## 4. Review and approval
Issues with status **In review** are discussed at the expert group meetings. The review can include testing the new knowledge model in the preproduction server of the web services of the SI Digital Framework (only available within the BIPM intranet and to external whitelisted IP addresses).

**Rephrase**
When a code patch is considered finished, the feature branch should merge all the changes done in branch `origin/develop` (*CP: or to rebase?*), All merging conflicts must be solved before creating a pull request; then the status of the issue is changed to **In review** at the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6).

> We do not need to all meet for small changes. BIPM Staff can decide merge requests to develop branches, CP: notify other expert group members, add a window for comments on one week, AS: supports. DC: no answers will mean everybody agrees?
> 
> 

If the expert group members reach a consensus that an implementation is suitable and complete, the changes are merged into branch `origin/develop,` and the feature/fix branch is deleted. A comment is added to the webpage of the issue and its status is changed to **Awaiting release** on the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6). The summary of the implementations is updated in the release notes of the repository.


## 5. Release
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

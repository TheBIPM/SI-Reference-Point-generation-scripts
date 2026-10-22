# Governance model for updating the SI Reference Point
> *This document is in draft form.*
#### Table of Contents
[1. Document objectives and scope](#1-document-objectives-and-scope)  
[2. General overview of the SI Reference Point](#2-general-overview-of-the-si-reference-point)  
[3. Stages for change requests of the SIRP](#3-stages-for-change-requests-of-the-sirp)  
[4. Change management](#4-change-management)


## 1. Document objectives and scope
This document specifies the governance model for the SI Reference Point (SIRP), a service developed and maintained under the auspices of the BIPM.
It sets out how change requests and bug reports are processed, covering the full path from the initial change request to the release of an updated version.
It establishes labelling conventions for releases, principles for the development process and the review procedure before the update is released.
It also defines the responsibilities and competences of the Expert Group of the FORUM-MD Task Group on SI Digital Framework [FORUM-MD-TG-SIDF](https://www.bipm.org/en/committees/fo/forum-md/wg/forum-md-tg-sidf).
The document does not describe the SIRP in full but only gives a short overview of the service.
For a full description, please refer to [Gruber et. al., 2026 - UNPUBLISHED]().

  
## 2. General overview of the SI Reference Point

The SI Reference Point (SIRP) is a machine-actionable knowledge model of the [SI Brochure](https://doi.org/10.59161/AUEZ1291).
The SIRP is developed by the members of the Expert Group of the FORUM-MD-TG-SIDF, under the auspices of the BIPM.  
The web services available at [https://si-digital-framework.org/SI](https://si-digital-framework.org/SI) provide access to the knowledge model of the SIRP.
The web services are developed by the BIPM, consulting with members of the Expert Group when considered necessary.  
  
The project is handled at two public GitHub repositories that serve different purposes:
- [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts):
    A Python package that generates the knowledge graph of the SIRP serialized as Turtle and JSON-LD files.
- [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework):
    A read-only repository to track changes in the Turtle-serialized files of the SIRP and other related ontologies published by the BIPM.

Releases of the SIRP are versioned according to the [Semantic Versioning scheme](https://semver.org/), using three dot-separated integer numbers known as the major, minor and patch version (see [below](#updatetype)).

## 3. Stages for change requests of the SIRP
Changes of the SIRP respond to feedback received from the user community.
Each request will go through stage 1, 2 and 6.
If it is decided to implement a change, it goes also through stages 3 to 5:

1.  Reception and registration of a request
2.  Classification, assessment and prioritization
3.  Development
4.  Review and approval
5.  Release
6.  Close the request

The individual stages are further described below.
A [diagram of the process](#diagram-of-the-process) is provided at the end of the document.

<a name="note1"></a>
> **Note:**
    The procedures stated in this governance document apply to requests related to the SIRP (the knowledge model).
    Issues related to the web services or to the management of the repository are handled by the BIPM staff, who may nonetheless choose to apply some of these procedures at their own discretion.

### 3.1 Reception and registration of a request
Changes to the SIRP may be necessary when reference documents (primarily the SI Brochure) are updated, when errors in the knowledge base are identified, or when new feature requests arise.
All change requests should be recorded as issue on the GitHub repository.
Before opening a new issue, it should be checked if an existing issue relates to the same topic.
If there is a related issue, the new information should be added as a comment to the discussion thread of the existing issue.

Issues can be raised by different groups of people.
In some cases, the origin of the issue is added to the issue as label:
- a representative of the corresponding digitalization working group of a CIPM Consultative Committee (label `request-from-CC`)
- a representative of a FORUM-MD working group (label `request-from-FORUM-MD`)
- a representative of a liaison organization (label `request-from-liaison-org`).
- any user of the SIRP from the community (no label required)

A change requests can be deposited directly by raising a GitHub issue, by sending an email or by verbal communication to a member of the Expert Group (e.g. during meetings).
Every requests must be linked to a requester, either an individual or a body (e.g. working group of a CIPM Consultative Committee).
Requests that are not submitted  as a GitHub issue shall still be registered as GitHub issue in either of the two public repositories by a member of the Expert Group.  
If a person submits a request on behalf of someone else, the information *on behalf of* should be included in the new issue.
In this case, the URL of the GitHub issue is shared with the person who originally made the request.

Requestors are encouraged to propose a scope label (see [3.2.1 Scope labels](#321-scope-labels)) for the issue they raise.
Adding information about the origin and the scope of the issue is useful when deciding the priority of the topics.


### 3.2 Classification, assessment and prioritization
Requests are managed in the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6), which provides a dashboard to follow up on the status of the requests.
The dashboard is accessible to members of the Expert Group.
View-only access can be granted to members of the Forum-MD-TG-SIDEF upon request.

Every duly recorded issue must have three additional labels: a scope label, a priority label and a status label.

#### 3.2.1 Scope labels
The scope label helps to identify and to prioritize the issue.
The scope can be suggested by the requestor and is decided decided by the Expert Group.  

Possible scope labels are:
| Issues related to| Label          | 
|:-------|:--------|
| Ontology| `scope-ontology` |
| Web services | `scope-web-services`|
| Management of the repository| `scope-repo-management` |
| Python package, not causing any effect on the ontology itself | `scope-python-package` |
| Questions that do not require any changes| `scope-question` |

<a name="note2"></a>
> **Note:**
    The issue of the last type (Questions) can be closed immediately after an answer has been provided.

#### 3.2.2 Priority label    
Priority labels give an indication on how urgent an issue is. 
The Expert Group assesses and prioritize issues related to the knowledge model and sets a priority label to each issue.

| Priority | Label          | 
|:-------|:--------|
| low | `priority-low` |
| medium | `priority-medium` |
| high | `priority-high` |

#### 3.2.3 Status label
The status label helps to track the progress being made with a specific issue.
The status are successive steps in the handling of an issue.
Not all issues must necessarily go through all steps.   

At every meeting of the Expert Group the issues in the dashboard of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) are discussed and reorganized in status boxes.
The meaning of each status is described below:


| Status | Label | Following to status |
|:---------------|:--------------|:-----------|
| [Backlog](#backlog) | `status-backlog` | Planned, Consultation, Not planned |
| [Planned](#planned)| `status-planned`| Consultation, In progress |
| [Consultation](#consultation)| `status-consultation` | Planned, Not planned |
| [In progress](#in-progress)| `status-in-progress` | In review |
| [In review](#in-review)| `status-in-review` | In progress, Awaiting release |
| [Awaiting release](#awaiting-release)| `status-awaiting-release` | Done | 
| [Done](#done)| `status-done` | - |
| [Not planned](#not-planned)| `status-not-planned` | - | 


<div style="padding-left: 50px; padding-right: 50px;" markdown="1">

---
#### Backlog
Every issue starts with this status, meaning that it has been registered and may contain additional comments, but no decision on prioritization or implementation has been made.
The issues registered in the repository [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) are added automatically to the [Backlog](#backlog), while those registered in the repository [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework) must be imported manually.
Optionally, issues from other private repositories (e.g. related to the web services) can be added here to ease the follow-up of topics.

The issues in the [Backlog](#backlog) are discussed during the meetings of the Expert Group and may thereafter be assigned the status [Planned](#planned), [Consultation](#consultation), or [Not planned](#not-planned), depending on the conclusion from the participants in the meeting.
Before moving any issue from this box, a comment is added with a summary of the outcomes of the discussion.

---
#### Planned
This status is assigned to issues that have been considered feasible and necessary by the Expert Group.
This status means that the Expert Group undertakes to advance the issue in due time. 
This status may also be assigned to requests previously in [Consultation](#consultation), depending on the feedback that was collected from another body.

At this stage, the Expert group assigns a priority level to the issue (see [3.2.2 Priority label](#322-priority-label))

Depending on the prioritization and complexity level of the issue, one or more Expert Group members may volunteer to work on the code implementation depending on their availability and area of expertise.
This delegation is declared on the webpage of the issue using the GitHub function *Assignees*.

The type of update that will potentially result as a consequence of implementing the solution to the request must be estimated and declared by adding a corresponding label. The following rules are adapted from the [Semantic Versioning scheme](https://semver.org/):
<a name="updatetype"></a>
- `possible-update-major`:
    A change will introduce incompatibility with former versions of the knowledge model (e.g. eliminating a class, renaming a datatype property).
- `possible-update-minor`:
    A feature will be introduced in a backward-compatible manner (e.g. adding new individuals, like new units of measurement).
- `possible-update-patch`:
    A bug will be fixed in a backward-compatible manner (e.g. fixing a comment or relabelling an individual).

Changes that will likely involve a major version update must be discussed and approved at the TG-SIDF, which might decide to further discuss the implications with other groups of the FORUM-MD or a CIPM Consultative Committee (see Section [4. Review and approval](#4-review-and-approval)).
During this time the issue is moved to [Consultation](#consultation).
The label for the possible type of update can be modified during the development of the solution to a request.

When the code implementation is ready to begin, the issue is moved to the status [In progress](#in-progress).

---
#### Consultation
This status is assigned to issues for which the Expert Group considers a discussion within another body necessary before a decision can be made.
The reason for consultation can be strong disagreement within the Expert Group or a level of decision competence that goes beyond the Expert Group (e.g. an update that would lead to a major update).

The default body to consider for consultation is the FORUM-MD-TG-SIDF.
However, the Expert Group can also decide to discuss the topic directly with another working group of the FORUM-MD, the Consultative Committee for Units (CCU), or another Consultative Committee of the CIPM.
A member of the Expert Group must be designated as responsible for doing the consultation. 
When the information has been gathered, a summary must be added as a comment to the issue webpage.
After discussing the newly collected information, the issue can be assigned the status [Planned](#planned) or [Not planned](#not-planned).

---
#### In progress
This status is assigned to issues for which the Expert Group decides to start working on the code implementation to address them.

The details of this stage are given in Section [3.3 Development](#33-development).
When the code implementation is considered finished, the issue is assigned the status [In review](#in-review).

---
#### In review
This status is assigned to issues for which the people working on a request consider that the code implementation is completed and the proposed solution should be reviewed, either by the Expert Group or by a different body. 

The details of the review stage are given in Section [3.4. Review and approval](#34-review-and-approval).
Depending on the outcome of the review, the issue can be moved back to status [In progress](#in-progress), or advanced to status [Awaiting release](#awaiting-release).

---
#### Awaiting release
This status is assigned to issues that have successfully completed the review process, either by the Expert Group or by a different body.
This status means that the request will be solved on the next release of the SIRP. 

The details of this stage are given in Section [3.5. Release](#35-release).
After the release has been done, the issue is advanced to the latest status [Done](#done).

---
#### Done
This status is achieved to issues that were marked [Awaiting release](#awaiting-release), after the updated knowledge model of the SIRP has been released.
The issues moved to this status box can be closed as completed and the person who originally made the request is notified.

---
#### Not planned
This status is assigned to issues from the boxes [Backlog](#backlog) or [Consultation](#consultation), when the corresponding decision body has considered them unsuitable under current circumstances.
The person or body who originally made the change request is notified about the decision not to proceed with the request, with a summary of the reasons considered.

The issues here are assigned the label `status-not-planned` and must be closed (GitHub function *Close as not planned*) on the issue webpage.

---
</div>




### 3.3 Development
The development is done in the repository [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts).
This section describes the guidelines for branching and merging.

#### 3.3.1. Branching
The repository will always hold two permanent branches: 

* Branch `origin/main`:
    Always reflects the version of the Python package that generates the latest stable release of the SIRP, available both on the [website of the SI Digital Framework](https://si-digital-framework.org/) and in the [read-only repository of the SI Digital Framework](https://github.com/TheBIPM/SI_Digital_Framework).
* Branch `origin/develop`:
    Contains the latest feature implementations and bug fixes that have been approved for the next release of the SIRP.

To start working on an issue that was [Planned](#planned), a member of the Expert Group creates a branch (feature branch) that will have a limited lifetime.
The feature branches are created from the branch `origin/develop` and should be named in an informative way, including the number of the issue when possible.
For example, a good name for the [issue #95](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts/issues/95) that relates to version 4.01 of the 9th edition of the SI Brochure could be `95-new-version-of-the-9th-edition-of-the-si-brochure-v4_01`.
A single feature branch can be used to work on more than one issue.
The URL of the feature branch must be referenced in the webpage of the issues, either automatically by a GitHub workflow, or manually in a comment by the person creating the branch.

The issues that have an active branch should be assigned the status [In progress](#in-progress).

#### 3.3.2. Contributions from outside the Expert Group
Members of the broader community who do not have write access to the repository can still contribute by first creating a fork of [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) under their own GitHub account.
Feature branches are then created within this fork, following the same conventions described in Section [3.3.1. Branching](#331-branching).
Once the proposed changes are ready, a pull request can be opened from the forked branch into the `origin/develop` branch of the main repository, as described in Section [3.3.3. Opening a pull request](#333-opening-a-pull-request).

#### 3.3.3 Opening a pull request
When the code patch that addresses an issue is considered finished by the developers, they change the status of the issue to [`status-in-review`](#in-review) and signal completion of the development by opening a pull request into the branch `origin/develop`.
Only when the review process is completed can the update by integrated in the `origin/develop` branch. 

All merging conflicts must be resolved before creating a pull request.
The URLs of the issues that are tackled by a pull request shall be mentioned in the pull request message or in a comment to the pull request.


### 3.4. Review and approval
Every pull request to branch `origin/develop` is initially reviewed by BIPM staff.
The changes must be assessed thoroughly to check if their implementation maintains a backward-compatible or not. 
This assessment should consider potential effects on other BIPM digital services that rely on the SIRP, like the Key Comparison Database (KCDB).
The type of update (patch, minor or major update) associated with an issue might change as a consequence of this assessment. 

The approval process depends on the type of update. 

#### 3.4.1. Issues labelled as `possible-update-minor` and `possible-update-patch`
After confirming that the changes maintain backward compatibility,

 >*__Here we need to decide on one of the following approaches__*

|*Option 1: Direct approval by BIPM staff*| *Option 2: Notice period before approval*|
|---|---|
|The pull request is approved at BIPM staff's discretion, with further consultation with other members of the Expert Group when considered necessary. The change is notified to all members of the Expert Group by email on a regular basis, including the links to the corresponding pull request. The Expert Group members are encouraged to comment on the closed pull request. In case of unresolved disagreement, the discussion is held at the Expert Group meetings.  | Expert Group members are informed by email of open pull requests. They are encouraged to comment in case of suggestions or disagreement. After a period of at least seven calendar days, the pull request can be approved by BIPM staff.|

All changes to the branch `origin/develop` can be reverted in case it is considered necessary.

The issues for which a pull request has been merged to the branch `origin/develop` should be assigned the status [Awaiting release](#awaiting-release).
If the changes are not approved, the feature branch is not merged, and the issue is returned to [In progress](#in-progress).


#### 3.4.2. Issues labelled as `possible-update-major`
The outcome of the changes that imply a major update of the knowledge model should be discussed at the FORUM-MD-TG-SIDF meeting.
The implications of the changes may be discussed with other working groups of the FORUM-MD, or with other CIPM Consultative Committees. 
If the changes are approved, the feature branch is merged into the branch `origin/develop`, and the issues are assigned the status [Awaiting release](#awaiting-release).
The communities that may be affected by the major update shall be notified accordingly.
If the changes are not approved, the feature branch is not merged, and the issue is returned to [In progress](#in-progress).

### 3.5. Release
After the approval of the update is done at the corresponding body, the release of the updated version of the SIRP includes the following steps:

1.  Assignment of a version number.
2.  Drafting of release notes, summarizing the changes made to the knowledge model since the latest release.
3.  Circulation of the release notes to the FORUM-MD-TG-SIDF members by email, along with the updated knowledge model serialized as Turtle files.
4.  A period of seven calendar days is given to raise any objections regarding the update of the knowledge model.
5.  During this time:
    5.1.  If there are no objections, the changes in branch `origin/develop` are merged into the branch `origin/main` and the release process can advance.
    5.2.  If there are objections, the comments may be addressed and the amendments circulated again for consultation to the FORUM-MD-TG-SIDF members. If there are still objections, the topic should be further discussed at the following meeting of the FORUM-MD-TG-SIDF and the release is paused.
6.  A GitHub release is done in the [generation scripts repository](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) including the files of the knowledge model, serialized both as Turtle and JSON-LD formats, in the field for *binaries*.
7.  The Turtle files are updated in the [SI Digital Framework repository](https://github.com/TheBIPM/SI_Digital_Framework).
8.  The web services of the [SI Digital Framework website](https://si-digital-framework.org/) are restarted with the updated SIRP.
9.  A successful release is indicated to the community by using the BIPM communications channels, as considered appropriate by the TG-SIDF chair.
10. The people whose requests were satisfied with the release of the SIRP are notified.

Previous versions of the SIRP remain accessible by using the version URIs.
The canonical URLs (without version number) resolve to the latest released version of the SIRP.

## 4. Change management
Changes to procedure of this document must be approved by the FORUM-MD-TG-SIDF.
| Date | Change    | 
|:-------|:--------|
| 2026-11-25 | Initial version, approved by FORUM-MD-TG-SIDF.|




## Diagram of the process
``` mermaid
flowchart TB
    REQ["Request received<br>GitHub issue, email, meeting"] --> DUP{"Related issue<br>already open?"}
    DUP -- Yes --> CMT["Add comment to existing issue"]
    DUP -- No --> NEW@{ label: "Register new issue.<br>Add *'On behalf of…'* if needed" }
    CMT --> BL["`**Backlog**<br>Classify: scope (mandatory),<br>requesting body (optional)`"]
    NEW --> BL
    BL --> EG{"Expert Group<br>meeting"}
    BL -- label 'question' --> QA["Answer and close"]
    EG -- Feasible & necessary --> PL["`**Planned**<br>Priority label, assignees,<br>possible-update-major/minor/patch`"]
    EG -- Unsuitable --> NP["`**Not planned**<br>Notify requester with reasons,<br>close as not planned`"]
    EG -- "High-level decision needed <br>or strong disagreement" --> CO["`**Consultation**<br>TG-SIDF, FORUM-MD WG,<br>CCU or other CC`"]
    CO -- Findings: unsuitable --> NP
    CO -- Findings: approved ---> PL
    PL -- Feature branch from develop --> IP["`**In progress**`"]
    IP -- Pull request to develop --> IR["`**In review**<br>BIPM staff check backward<br>compatibility, KCDB impact`"]
    IR --> IMP{"Impact?"}
    IMP -- Minor / patch --> BS{"BIPM staff<br>approval?"}
    IMP -- Major --> TG{"TG-SIDF<br>approval?"}
    BS -- No --> IP
    TG -- No --> IP
    BS -- Yes: merge to develop --> AR["`**Awaiting release**`"]
    TG -- Yes: merge to develop,<br>notify affected communities --> AR
    AR --> RN["Version number, release notes,<br>circulate to TG-SIDF with Turtle files"]
    RN --> OBJ{"Objections within<br>7 calendar days?"}
    OBJ -- Yes --> AC["Address comments<br>Expert Group or TG-SIDF meeting"]
    AC --> RN
    OBJ -- No --> PUB["Merge develop → main<br>GitHub release (Turtle + JSON-LD)<br>Update SI_Digital_Framework repo<br>Restart web services, announce"]
    PUB --> DN["`**Done**<br>Close issue, notify requester`"]

    NEW@{ shape: rect}
     BL:::status
     QA:::terminal
     PL:::status
     NP:::reject
     CO:::status
     IP:::status
     IR:::status
     AR:::status
     DN:::terminal
    classDef status fill:#e8f0fe,stroke:#1a56db,stroke-width:2px
    classDef terminal fill:#e6f4ea,stroke:#137333,stroke-width:2px
    classDef reject fill:#fce8e6,stroke:#c5221f,stroke-width:2px
```

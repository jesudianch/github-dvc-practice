# github-dvc-practice
'''
1.GitHub Repository Link
 https://github.com/jesudianch/github-dvc-practice
2.Provide the URL to your github-dvc-practice repository.

3.Commit History
(base) jesudianchallapalli@Jesudians-MacBook-Air-2 github-dvc-practice % git log
commit 01e3b3aa4d86d7c7a682395ae2ae2c0fd61f4ac0 (HEAD -> feature/greeting, origin/feature/greeting)
Author: jesudianch <jchallapalli7@gmail.com>
Date:   Tue Feb 18 16:16:46 2025 -0500

    Update sample dataset with new entry

commit b7bf98483b8343625639e719e68967de599a2041
Author: jesudianch <jchallapalli7@gmail.com>
Date:   Mon Feb 17 21:47:28 2025 -0500

    Update sample dataset with new entry

commit 827b82bab27bdcef9ea62fff203b8bae76a692e8
Author: jesudianch <jchallapalli7@gmail.com>
Date:   Mon Feb 17 21:41:13 2025 -0500

    Track sample dataset with DVC

commit 2fece48e1d76396531a2803e3a28418013536ad7
Author: jesudianch <jchallapalli7@gmail.com>
Date:   Mon Feb 17 21:37:27 2025 -0500

    modify the file

commit 9fb191aaca850109eaff11d23cc7ef8c232b9e9e
Author: jesudianch <jchallapalli7@gmail.com>
Date:   Mon Feb 17 17:06:34 2025 -0500

Blockers: When I tried to checkout from feature/Greeting to Main I'm getting following error

base) jesudianchallapalli@Jesudians-MacBook-Air-2 github-dvc-practice % git checkout main
error: Your local changes to the following files would be overwritten by checkout:
        .DS_Store
Please commit your changes or stash them before you switch branches.
Aborting

4. Collobaration step Blocker

(base) jesudianchallapalli@Jesudians-MacBook-Air-2 collaborator % dvc pull
Collecting                                                                                         |1.00 [00:00,  557entry/s]
WARNING: Some of the cache files do not exist neither locally nor on remote. Missing cache files:
md5: 4e1d0d2a0773826d273b9bf8658a9b29                                                                                        
Fetching
Building workspace index                                                                           |1.00 [00:00,  910entry/s]
Comparing indexes                                                                                 |3.00 [00:00, 3.06kentry/s]
Applying changes                                                                                   |0.00 [00:00,     ?file/s]
Everything is up to date.
ERROR: failed to pull data from the cloud - Checkout failed for following targets:
data/sample_data.csv
Is your cache up to date?
<https://error.dvc.org/missing-files>

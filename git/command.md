# 명령어 정리

## `git init`
- 현재 디렉토리에 `.git` 폴더를 생성하여 새로운 Git 저장소를 초기화.

## `git clone`
- 현재 디렉토리에 원격저장소 폴더를 복제.

```
git clone {remote-url}
git clone {remote_url} {directory_name}
```

## `get status`
- 현재 git 상태를 확인


## `git add`
- workinig directory에서 변경된 파일을 staging area에 이동

```
git add {file_name/directory_name}
git add. => 현재 나의 위치를 기준으로 모든 파일과 폴더
```

## `git commit`
- staging area에 있는 변경사항을 커밋하여 스냅샷 생성

## `git log`
- 커밋의 히스토리를 조회(사진들의 목록을 보는 명령어)
    - option
        - `--oneline`
        - `--graph`

## `git remote`
- 원격저장소 관리 명령어

- 원격저장소 추가하는 명령어
    - 일반적으로 remote_name은 `origin` 사용
```
git remote add {remote_name} {remote_url}
```

- 원격저장소 확인
```
git remote -v
```

- 원격저장소 삭제
```
git remote remove {remote_name}
```


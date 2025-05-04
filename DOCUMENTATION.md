# Сгенерированная документация

## Модуль [`rag/rag_service.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/rag/rag_service.py)

_Докстрока отсутствует._

### Класс `QueryRequest`


_Докстрока отсутствует._

### Функция `retrieve_similar_code(query, top_k=5)`


_Докстрока отсутствует._

### Функция `build_llm_input(query, structures)`


_Докстрока отсутствует._

### Функция `rag_query(req)`


_Докстрока отсутствует._

## Модуль [`diagramParser/main.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/diagramParser/main.py)

_Докстрока отсутствует._

### Класс `RepoRequest`


_Докстрока отсутствует._

### Класс `C4Response`


_Докстрока отсутствует._

### Функция `generate_diagram(data)`


1) Клонируем репозиторий из data.repo_url
2) Строим граф и конвертим его в формат C4
3) Возвращаем JSON с ключами containers, components, relationships

## Модуль [`diagramParser/static_analyzer.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/diagramParser/static_analyzer.py)

_Докстрока отсутствует._

### Класс `StaticRepoParser`


_Докстрока отсутствует._

### Функция `__init__(self, repo_url, clone_dir=None)`


_Докстрока отсутствует._

### Функция `clone_repo(self)`


Клонируем репозиторий

### Функция `cleanup(self)`


Удаляем временную папку

### Функция `_collect_py_files(self)`


_Докстрока отсутствует._

### Функция `build_graph(self)`


_Докстрока отсутствует._

### Функция `graph_to_c4(self, graph)`


_Докстрока отсутствует._

### Класс `CallVisitor`


_Докстрока отсутствует._

### Функция `__init__(self, graph, current)`


_Докстрока отсутствует._

### Функция `visit_Call(self, call)`


_Докстрока отсутствует._

## Модуль [`llm_analysis/to_mermaid.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/llm_analysis/to_mermaid.py)

_Докстрока отсутствует._

### Функция `sanitize(id_str)`


_Докстрока отсутствует._

## Модуль [`llm_analysis/app/config.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/llm_analysis/app/config.py)

_Докстрока отсутствует._

## Модуль [`llm_analysis/app/diagram.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/llm_analysis/app/diagram.py)

_Докстрока отсутствует._

### Класс `DiagramBuilder`


Принимает summary от RepoParser и строит C4-диаграмму с обогащенными описаниями через Yandex GPT.

### Функция `__init__(self, summary)`


_Докстрока отсутствует._

### Функция `build_c4(self)`


_Докстрока отсутствует._

## Модуль [`llm_analysis/app/main.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/llm_analysis/app/main.py)

_Докстрока отсутствует._

### Функция `generate_diagram(req)`


_Докстрока отсутствует._

## Модуль [`llm_analysis/app/models.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/llm_analysis/app/models.py)

_Докстрока отсутствует._

### Класс `RepoRequest`


_Докстрока отсутствует._

### Класс `ContainerModel`


_Докстрока отсутствует._

### Класс `ComponentModel`


_Докстрока отсутствует._

### Класс `RelationshipModel`


_Докстрока отсутствует._

### Класс `DiagramResponse`


_Докстрока отсутствует._

## Модуль [`llm_analysis/app/parser.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/llm_analysis/app/parser.py)

_Докстрока отсутствует._

### Класс `RepoParser`


Клонирует репозиторий, поуровнево суммирует код (функции → файлы → репозиторий)
с помощью Yandex GPT и возвращает структурированные summary.

### Функция `__init__(self, repo_url, clone_dir=None)`


_Докстрока отсутствует._

### Функция `clone_repo(self)`


Клонирует Git-репозиторий в временную папку

### Функция `cleanup(self)`


Удаляет временную папку с репозиторием

### Функция `extract_code_blocks(self)`


Ищет в .py-файлах репозитория определения функций, async-функций и классов,
возвращает список кортежей (key, code), где key = "path:Name".

### Функция `summarize_all(self)`


1) Суммирует каждый кодовый блок (функция/класс)
2) Группирует их по файлам и суммирует файлы
3) Дает общий обзор репозитория
Возвращает dict с keys: block_summaries, file_summaries, repo_summary.

## Модуль [`llm_analysis/app/static_analyzer.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/llm_analysis/app/static_analyzer.py)

_Докстрока отсутствует._

### Класс `StaticRepoParser`


_Докстрока отсутствует._

### Функция `__init__(self, repo_url, clone_dir=None)`


_Докстрока отсутствует._

### Функция `clone_repo(self)`


Клонируем репозиторий

### Функция `cleanup(self)`


Удаляем временную папку

### Функция `_collect_py_files(self)`


_Докстрока отсутствует._

### Функция `build_graph(self)`


_Докстрока отсутствует._

### Функция `graph_to_c4(self, graph)`


_Докстрока отсутствует._

### Класс `CallVisitor`


_Докстрока отсутствует._

### Функция `__init__(self, graph, current)`


_Докстрока отсутствует._

### Функция `visit_Call(self, call)`


_Докстрока отсутствует._

## Модуль [`llm_analysis/app/yandex_gpt.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/llm_analysis/app/yandex_gpt.py)

_Докстрока отсутствует._

### Класс `YandexGPTClient`


_Докстрока отсутствует._

### Функция `__init__(self)`


_Докстрока отсутствует._

### Функция `summarize(self, prompt, max_tokens=300)`


_Докстрока отсутствует._

## Модуль [`common/__init__.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/__init__.py)

_Докстрока отсутствует._

## Модуль [`common/s3/base.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/s3/base.py)

_Докстрока отсутствует._

### Функция `get_s3_connection()`


_Докстрока отсутствует._

## Модуль [`common/s3/dependency.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/s3/dependency.py)

_Докстрока отсутствует._

### Функция `get_s3()`


_Докстрока отсутствует._

## Модуль [`common/s3/download.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/s3/download.py)

_Докстрока отсутствует._

### Функция `get_file(subfolder, file_path)`


Получаем код из Minio по пути файла

## Модуль [`common/ast/pipeline.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/ast/pipeline.py)

_Докстрока отсутствует._

### Класс `CacheManager`


Управление кэшированными AST и метаданными (Git-хеши файлов).
Если репозиторий недоступен из-за прав, кэширование отключается.

### Класс `CodeParser`


Парсинг Python-файлов в AST с поддержкой кэша.

### Класс `Indexer`


Построение FAISS-индекса эмбеддингов AST-фрагментов и узлов графа.

### Функция `__init__(self, repo_path, cache_dir='.cache')`


_Докстрока отсутствует._

### Функция `_cache_path(self, file_path)`


_Докстрока отсутствует._

### Функция `is_cached(self, file_path)`


_Докстрока отсутствует._

### Функция `is_modified(self, file_path)`


_Докстрока отсутствует._

### Функция `load_ast(self, file_path)`


_Докстрока отсутствует._

### Функция `save_ast(self, file_path, ast_node)`


_Докстрока отсутствует._

### Функция `__init__(self, repo_path, cache_manager=None)`


_Докстрока отсутствует._

### Функция `find_py_files(self)`


_Докстрока отсутствует._

### Функция `parse_file(self, file_path)`


_Докстрока отсутствует._

### Функция `parse_repo(self)`


_Докстрока отсутствует._

### Функция `ast_to_text(self, node)`


_Докстрока отсутствует._

### Функция `extract_calls(self, node)`


Извлечение пар (caller, callee) из AST-функций.

### Функция `__init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2')`


_Докстрока отсутствует._

### Функция `build_index(self, texts)`


_Докстрока отсутствует._

### Функция `add_metadata(self, meta)`


_Докстрока отсутствует._

### Функция `save_index(self, index_path, meta_path)`


_Докстрока отсутствует._

### Функция `load_index(self, index_path, meta_path)`


_Докстрока отсутствует._

## Модуль [`common/qdrant/base.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/qdrant/base.py)

_Докстрока отсутствует._

### Функция `get_qdrant_connection()`


_Докстрока отсутствует._

## Модуль [`common/qdrant/collections.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/qdrant/collections.py)

_Докстрока отсутствует._

### Функция `ensure_collection_exists(collection_name)`


Проверяем, существует ли коллекция, и baseсоздаем её, если не существует.

## Модуль [`common/qdrant/dependency.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/qdrant/dependency.py)

_Докстрока отсутствует._

### Функция `get_qdrant()`


_Докстрока отсутствует._

## Модуль [`common/schemas/__init__.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/schemas/__init__.py)

_Докстрока отсутствует._

## Модуль [`common/schemas/project.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/schemas/project.py)

_Докстрока отсутствует._

### Класс `Project`


_Докстрока отсутствует._

## Модуль [`common/schemas/user.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/schemas/user.py)

_Докстрока отсутствует._

### Класс `User`


_Докстрока отсутствует._

## Модуль [`common/database/base.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/database/base.py)

_Докстрока отсутствует._

### Функция `get_database_connection()`


_Докстрока отсутствует._

## Модуль [`common/database/dependency.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/database/dependency.py)

_Докстрока отсутствует._

### Функция `get_db()`


_Докстрока отсутствует._

## Модуль [`common/auth/dependency.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/auth/dependency.py)

_Докстрока отсутствует._

### Функция `get_current_user(creds=Depends(security), db=Depends(get_db))`


_Докстрока отсутствует._

## Модуль [`common/auth/policy.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/common/auth/policy.py)

_Докстрока отсутствует._

## Модуль [`ingest/ingest_service.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/ingest/ingest_service.py)

_Докстрока отсутствует._

### Класс `IngestRequest`


_Докстрока отсутствует._

### Функция `ingest_repository(request, minio_client=Depends(get_s3), qdrant_client=Depends(get_qdrant))`


_Докстрока отсутствует._

### Функция `download_repository(url)`


Скачиваем репозиторий с использованием Git

### Функция `split_repository(repo_dir)`


Разбиение репозитория на AST и байткод

### Функция `extract_defs_from_file(file_path, repo_path)`


Извлечение функций и классов из исходного файла Python

### Функция `parse_bytecode(bytecode, file_path)`


Парсинг байткода для извлечения инструкций

### Функция `extract_vectors(ast_data)`


_Докстрока отсутствует._

### Функция `embed_texts(texts, batch_size=50)`


_Докстрока отсутствует._

## Модуль [`user_service/main.py`](https://github.com/shashliki-ot-dushi/beeline-case/blob/main/user_service/main.py)

_Докстрока отсутствует._

### Класс `SessionResponse`


_Докстрока отсутствует._

### Класс `ProjectCreate`


_Докстрока отсутствует._

### Класс `ProjectResponse`


_Докстрока отсутствует._

### Функция `get_current_user(creds=Depends(security), db=Depends(get_db))`


_Докстрока отсутствует._

### Функция `create_session(db=Depends(get_db))`


Create a new user session.
Returns a UUID4 token to use as Bearer auth.

### Функция `list_projects(user=Depends(get_current_user), db=Depends(get_db))`


List all projects for the authenticated user.

### Функция `create_project(payload, user=Depends(get_current_user), db=Depends(get_db))`


Create a new project for the authenticated user.
Returns its UUID4 id.

### Функция `delete_project(project_id, user=Depends(get_current_user), db=Depends(get_db))`


Delete one of the authenticated user's projects.

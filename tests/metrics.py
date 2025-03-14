import re
import requests


def cgw_metric_get(host: str = "localhost", port: int = 8080) -> str:
    metrics = ""

    try:
        # Try to fetch metrics with 5 seconds timeout value
        r = requests.get(f"http://{host}:{port}/metrics", timeout=5)
        print("CGW metrics ret code: " + str(r.status_code))
        assert r is not None and r.status_code == 200, \
                f"CGW metrics is not available"
        metrics = r.text
    except Exception as e:
        print("CGW metrics: raised exception when tried to fetch metrics:" + e)
        raise Exception('CGW metrics fetch failed (Not running?)')

    return metrics


def cgw_metrics_get_active_shards_num() -> int:
    active_shards_num = 0
    metrics = cgw_metric_get()

    match = re.search(r"cgw_active_shards_num (\d+)", metrics)
    if match:
        active_shards_num = int(match.group(1))
        print(f"Active shards num: {active_shards_num}")
    else:
        print("Active shards num not found.")

    return active_shards_num


def cgw_metrics_get_connections_num() -> int:
    wss_connections_num = 0
    metrics = cgw_metric_get()

    match = re.search(r"cgw_connections_num (\d+)", metrics)
    if match:
        wss_connections_num = int(match.group(1))
        print(f"WSS conections num: {wss_connections_num}")
    else:
        print("WSS conections num not found.")

    return wss_connections_num


def cgw_metrics_get_groups_assigned_num() -> int:
    groups_assigned_num = 0
    metrics = cgw_metric_get()

    match = re.search(r"cgw_groups_assigned_num (\d+)", metrics)
    if match:
        groups_assigned_num = int(match.group(1))
        print(f"Groups assigned num: {groups_assigned_num}")
    else:
        print("Groups assigned num not found.")

    return groups_assigned_num


def cgw_metrics_get_group_infras_assigned_num(group_id: int) -> int:
    group_infras_assigned_num = 0
    metrics = cgw_metric_get()

    match = re.search(rf"cgw_group_{group_id}_infras_assigned_num (\d+)", metrics)
    if match:
        group_infras_assigned_num = int(match.group(1))
        print(f"Group {group_id} infras assigned num: {group_infras_assigned_num}")
    else:
        print(f"Group {group_id} infras assigned num not found.")

    return group_infras_assigned_num


def cgw_metrics_get_groups_capacity() -> int:
    groups_capacity = 0
    metrics = cgw_metric_get()

    match = re.search(r"cgw_groups_capacity (\d+)", metrics)
    if match:
        groups_capacity = int(match.group(1))
        print(f"Groups capacity: {groups_capacity}")
    else:
        print("Groups capacity.")

    return groups_capacity


def cgw_metrics_get_groups_threshold() -> int:
    groups_threshold = 0
    metrics = cgw_metric_get()

    match = re.search(r"cgw_groups_threshold (\d+)", metrics)
    if match:
        groups_threshold = int(match.group(1))
        print(f"Groups assigned num: {groups_threshold}")
    else:
        print("Groups assigned num not found.")

    return groups_threshold


def cgw_metrics_get_group_ifras_capacity() -> int:
    group_infras_capacity = 0
    metrics = cgw_metric_get()

    match = re.search(r"cgw_group_ifras_capacity (\d+)", metrics)
    if match:
        group_infras_capacity = int(match.group(1))
        print(f"Groups capacity: {group_infras_capacity}")
    else:
        print("Groups capacity.")

    return group_infras_capacity

from datetime import timezone, datetime

from django.contrib.auth.models import User
from ix.task_log.models import Agent, Task, TaskLogMessage
from faker import Faker

fake = Faker()


def fake_agent(**kwargs):
    name = kwargs.get("name", fake.unique.name())
    purpose = kwargs.get("purpose", fake.text())

    agent = Agent.objects.create(name=name, purpose=purpose)
    return agent


def fake_user(**kwargs):
    username = kwargs.get("username", fake.unique.user_name())
    email = kwargs.get("email", fake.unique.email())
    password = kwargs.get("password", fake.password())

    user = User.objects.create_user(username=username, email=email, password=password)
    return user


def fake_goal(**kwargs):
    data = {"name": fake.word(), "description": fake.text()[:50], "complete": False}
    data.update(kwargs)
    return data


def fake_task(**kwargs):
    user = kwargs.get("user") or fake_user()
    goals = kwargs.get("goals", [fake_goal() for _ in range(fake.random.randint(1, 5))])
    agent = kwargs.get("agent") or fake_agent()
    task = Task.objects.create(user=user, goals=goals, agent=agent)
    return task


def fake_command_reply(**kwargs):
    content = {
        "type": "ASSISTANT",
        "thoughts": {
            "text": "thought",
            "reasoning": "reasoning",
            "plan": ["short list of steps", "that conveys", "long-term plan"],
            "criticism": "constructive self-criticism",
            "speak": "thoughts summary to say to user",
        },
        "command": {"name": "echo", "args": {"output": "this is a test"}},
    }
    return fake_task_log_msg(role="assistant", content=content, **kwargs)


def fake_feedback_request(task: Task = None, message_id: int = None, **kwargs):
    if not message_id:
        message_id = fake_command_reply(task=task).id
    content = {"type": "FEEDBACK_REQUEST", "message_id": message_id}
    return fake_task_log_msg(role="assistant", content=content, **kwargs)


def fake_auth_request(
    task: Task = None, message_id: int = None, feedback: str = None, **kwargs
):
    if not message_id:
        message_id = fake_feedback_request(task=task).id
    content = {"type": "AUTH_REQUEST", "message_id": message_id}
    return fake_task_log_msg(role="user", content=content, **kwargs)


def fake_execute(
    task: Task = None, message_id: int = None, feedback: str = None, **kwargs
):
    if not message_id:
        message_id = fake_feedback_request(task=task)
    content = {"type": "EXECUTED", "message_id": message_id}
    return fake_task_log_msg(role="user", content=content, **kwargs)


def fake_feedback(
    task: Task = None, message_id: int = None, feedback: str = None, **kwargs
):
    if not message_id:
        feedback_request = fake_feedback_request(task=task)
        message_id = feedback_request.id
    content = {"type": "FEEDBACK", "message_id": message_id}
    return fake_task_log_msg(role="user", content=content, **kwargs)


def fake_authorize(
    task: Task = None, message_id: int = None, feedback: str = None, **kwargs
):
    if not message_id:
        message_id = fake_feedback_request(task=task)
    content = {"type": "AUTHORIZE", "message_id": message_id, "n": 1}
    return fake_task_log_msg(role="user", content=content, **kwargs)


def fake_continuous_toggle(enabled: int = 1, **kwargs):
    content = {"type": "CONTINUOUS", "enabled": enabled}
    return fake_task_log_msg(role="user", content=content, **kwargs)


def fake_task_log_msg_type(content_type, **kwargs):
    if content_type == "CONTINUOUS":
        return fake_continuous_toggle(**kwargs)
    elif content_type == "FEEDBACK":
        return fake_feedback(**kwargs)
    elif content_type == "AUTHORIZE":
        return fake_continuous_toggle(**kwargs)
    elif content_type == "EXECUTED":
        return fake_continuous_toggle(**kwargs)
    elif content_type == "ASSISTANT":
        return fake_command_reply(**kwargs)
    elif content_type == "SYSTEM":
        return fake_task_log_msg(**kwargs)
    elif content_type == "FEEDBACK_REQUEST":
        return fake_feedback_request(**kwargs)
    elif content_type == "AUTH_REQUEST":
        return fake_auth_request(**kwargs)


def fake_task_log_msg(**kwargs):
    # Get or create fake instances for Task and Agent models
    task = kwargs.get("task", Task.objects.order_by("?").first())
    agent = kwargs.get("agent", task.agent)

    # Generate random role choice
    role = kwargs.get("role", fake.random_element(TaskLogMessage.ROLE_CHOICES)[0])

    # Generate random content as JSON
    content = kwargs.get(
        "content",
        {"type": "SYSTEM", "message": "THIS IS A TEST"},
    )

    # Get or generate created_at timestamp
    created_at = kwargs.get(
        "created_at",
        datetime.now(),
    )

    # Create and save the fake TaskLogMessage instance
    task_log_message = TaskLogMessage(
        task=task,
        agent=agent,
        created_at=created_at,
        role=role,
        content=content,
    )

    task_log_message.save()
    return task_log_message

# Notes

## Project Structure

order_service/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── orders.py
│   │
│   ├── schemas/
│   │   └── order.py
│   │
│   ├── services/
│   │   └── order_service.py
│   │
│   ├── domain/
│   │   ├── models.py
│   │   └── events.py
│   │
│   ├── infrastructure/
│   │   ├── kafka/
│   │   │   ├── producer.py
│   │   │   └── topics.py
│   │   │
│   │   └── db/
│   │       └── repository.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   └── dependencies/
│       └── kafka.py
│
└── requirements.txt

## Schema and Domain

🧾 Schema = “form at the front desk”
Used to collect data
Strict format
For communication
🧠 Domain = “actual business inside the company”
Does real work
Knows rules
Independent of forms

## Order
- Order = state (what exists)
- Order {
    id: 123,
    user_id: 7,
    status: "created"
    }

## Event
- Event = fact (what happened)
- spread awareness
- Event {
    "event_type": "order.created",
    "order_id": 123,
    "user_id": 7
    }


## Schemas
- Event schema (service-to-service) used by:
    - payment service
    - shipping service
    - analytics service

- API schema (client-facing) Used by:
    - frontend
    - mobile apps
    - external clients
app/
  schemas/          → API (FastAPI layer)
    order.py

  events/           → Kafka / messaging contracts
    order.py

## Kafka
- Intermediary to facilitate exchange between our producers and consumers
- to run Apache kafka broker server, we use docker
- aiokafka (client library)
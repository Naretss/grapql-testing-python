from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry

# 🔹 ตัวอย่างข้อมูลจำลอง
fake_database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

@strawberry.type
class Query:
    @strawberry.field
    def get_name_by_account_id(self, account_id: int) -> str:
        return fake_database.get(account_id, "ไม่พบข้อมูล")

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

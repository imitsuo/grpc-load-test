from dotenv import load_dotenv
from locust import task

import grpc_user
from app.protos.pipeline.pipeline_pb2 import RequestAggregated
from app.protos.pipeline.pipeline_pb2_grpc import PipelineServiceStub
from rpc.base import generate_id_token

load_dotenv()

# # Start the dummy server. This is not something you would do in a real test.
# @events.init.add_listener
# def run_grpc_server(environment, **_kwargs):
#     gevent.spawn(start_server)


class TSGrpcUser(grpc_user.GrpcUser):
    # channel = get_channel()
    # stub = PipelineServiceStub(channel)
    # host = os.getenv("TS-GRPC")
     host = "localhost:50051"
    token = generate_id_token()
    stub_class = PipelineServiceStub

    @task
    def Execute(self):
        self.stub.ExecuteAggregated(
            request=RequestAggregated(
                levels={
                    "children": [],
                    "metadatas": [
                        {
                            "metadata_id": 4310014,
                            "variable": "size__southeast",
                            "is_inflated": False,
                        }
                    ],
                },
                output_variable="Sudeste",
                commands={
                    "frequency": "KEEP_ORIGINAL",
                    "frequency_method": "LAST_OF_PERIOD",
                    "variation": "CALC_OF_ORIGINAL",
                    "variation_method": "YEAR_OVER_YEAR",
                    "inflation": "ORIGINAL",
                    "marketshare": None,
                    "aggregation_method": "AGG_AVERAGE",
                },
            ),
            metadata=[("authorization", f"Bearer {self.token}")],
            timeout=20,
        )

#     ],
#     "metadatas": [],
# }

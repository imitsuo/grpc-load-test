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
    # host = "localhost:50051"
    host = "https://run-4i-stg-4casthub-ts-grpc-ht3a3o3bea-ue.a.run.app"
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


# {
#     "children": [
#         {
#             "children": [
#                 {
#                     "children": [],
#                     "metadatas": [
#                         {
#                             "metadata_id": 4368009,
#                             "variable": "familia3_goias",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4354015,
#                             "variable": "familia3_federal_district",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4384006,
#                             "variable": "familia3_mato_grosso_do_sul",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4380007,
#                             "variable": "familia3_mato_grosso",
#                             "is_inflated": false,
#                         },
#                     ],
#                 }
#             ],
#             "metadatas": [],
#         },
#         {
#             "children": [
#                 {
#                     "children": [],
#                     "metadatas": [
#                         {
#                             "metadata_id": 4396003,
#                             "variable": "familia3_minas_gerais",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4348015,
#                             "variable": "familia3_sao_paulo",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4408002,
#                             "variable": "familia3_espirito_santo",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4354016,
#                             "variable": "familia3_rio_de_janeiro",
#                             "is_inflated": false,
#                         },
#                     ],
#                 }
#             ],
#             "metadatas": [],
#         },
#         {
#             "children": [
#                 {
#                     "children": [],
#                     "metadatas": [
#                         {
#                             "metadata_id": 4316015,
#                             "variable": "familia3_amazonas",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4310015,
#                             "variable": "familia3_tocantins",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4370009,
#                             "variable": "familia3_rondonia",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4310016,
#                             "variable": "familia3_amapa",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4372010,
#                             "variable": "familia3_para",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4402002,
#                             "variable": "familia3_acre",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4394005,
#                             "variable": "familia3_roraima",
#                             "is_inflated": false,
#                         },
#                     ],
#                 }
#             ],
#             "metadatas": [],
#         },
#         {
#             "children": [
#                 {
#                     "children": [],
#                     "metadatas": [
#                         {
#                             "metadata_id": 4392003,
#                             "variable": "familia3_pernambuco",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4406001,
#                             "variable": "familia3_sergipe",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4382006,
#                             "variable": "familia3_bahia",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4350015,
#                             "variable": "familia3_alagoas",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4392004,
#                             "variable": "familia3_piaui",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4344015,
#                             "variable": "familia3_ceara",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4326016,
#                             "variable": "familia3_rio_grande_do_norte",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4374010,
#                             "variable": "familia3_maranhao",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4390005,
#                             "variable": "familia3_paraiba",
#                             "is_inflated": false,
#                         },
#                     ],
#                 }
#             ],
#             "metadatas": [],
#         },
#         {
#             "children": [
#                 {
#                     "children": [],
#                     "metadatas": [
#                         {
#                             "metadata_id": 4386005,
#                             "variable": "familia3_parana",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4384005,
#                             "variable": "familia3_rio_grande_do_sul",
#                             "is_inflated": false,
#                         },
#                         {
#                             "metadata_id": 4400001,
#                             "variable": "familia3_santa_catarina",
#                             "is_inflated": false,
#                         },
#                     ],
#                 }
#             ],
#             "metadatas": [],
#         },
#     ],
#     "metadatas": [],
# }

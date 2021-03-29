# This file is automatically generated from helloworld.proto, DO NOT EDIT!

import asyncio
import nats.aio

import nrpc
import nrpc.exc
from nrpc import nrpc_pb2

import helloworld_pb2 as helloworld__pb2


PKG_SUBJECT = "helloworld"
PKG_SUBJECT_PARAMS = []
PKG_SUBJECT_PARAMS_COUNT = 0


Greeter_SUBJECT = "Greeter"
Greeter_SUBJECT_PARAMS = []
Greeter_SUBJECT_PARAMS_COUNT = 0


class GreeterHandler:
    methods = {
        "SayHello": ("SayHello", 0, helloworld__pb2.HelloRequest, True, False, False),
    }

    def __init__(self, nc, server):
        self.nc = nc
        self.server = server

    def subject(self, method=">"):
        return ".".join(["helloworld", Greeter_SUBJECT, method])

    async def handler(self, msg):
        try:
            pkg_params, svc_params, mt_subject, tail = nrpc.parse_subject(
                PKG_SUBJECT,
                PKG_SUBJECT_PARAMS_COUNT,
                Greeter_SUBJECT,
                Greeter_SUBJECT_PARAMS_COUNT,
                msg.subject,
            )

            (
                mname,
                params_count,
                input_type,
                has_reply,
                void_reply,
                streamed_reply,
            ) = self.methods[mt_subject]
            mt_params, count = nrpc.parse_subject_tail(params_count, tail)

            method = getattr(self.server, mname)
            if input_type is not None:
                req = input_type.FromString(msg.data)
                mt_params.append(req)
            err = None
            if streamed_reply:
                await nrpc.streamed_reply_handler(
                    self.nc, msg.reply, method(*mt_params)
                )
                return
            try:
                rep = await method(*mt_params)
            except nrpc.exc.NrpcError as e:
                err = e.as_nrpc_error()
            except Exception as e:
                err = nrpc.exc.server_error(e)
            else:
                if isinstance(rep, nrpc.ClientError):
                    err = rep
                elif void_reply and rep is not None:
                    raise ValueError(
                        "Method %s implementation should return None" % mname
                    )
            if has_reply:
                if err is not None:
                    rawRep = b"\x00" + err.SerializeToString()
                elif rep is not None:
                    rawRep = rep.SerializeToString()
                else:
                    rawRep = b""
                await self.nc.publish(msg.reply, rawRep)
        except Exception as e:
            import traceback

            traceback.print_exc()
            print("Error in Greeter.%s handler:" % mname, e)


class GreeterClient:
    def __init__(
        self,
        nc,
    ):
        self.nc = nc

    async def SayHello(
        self,
        req,
    ):
        subject = PKG_SUBJECT + "." + Greeter_SUBJECT + "." + "SayHello"
        rawReq = req.SerializeToString()

        rawRep = await self.nc.timed_request(subject, rawReq, 5)
        if rawRep.data and rawRep.data[0] == 0:
            raise nrpc.exc.from_error(nrpc_pb2.Error.FromString(rawRep.data[1:]))
        return helloworld__pb2.HelloReply.FromString(rawRep.data)

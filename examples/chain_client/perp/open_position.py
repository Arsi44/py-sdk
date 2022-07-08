# Copyright 2022 Nibiru Labs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import logging

from nibiru import Sdk, Side

async def main() -> None:
    trader = Sdk.authorize("guard cream sadness conduct invite crumble clock pudding hole grit liar hotel maid produce squeeze return argue turtle know drive eight casino maze host")
    res = await trader.tx.perp.open_position(
        sender = trader.address,
        token_pair = "unusd:unibi",
        side=Side.BUY,
        quote_asset_amount="5",
        leverage="5",
        base_asset_amount_limit="5",
    )
    print(res)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())

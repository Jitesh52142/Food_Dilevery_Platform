class AnalyticsAdapter:
    async def track_event(self, event_name: str, data: dict):
        print(f"Tracked event: {event_name}")

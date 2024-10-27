# from textwrap import dedent
# from typing import AsyncGenerator, List, Optional, Dict
# from enum import Enum

# from app.agents.analyst import create_analyst
# from app.agents.reporter import create_reporter
# from app.agents.researcher import create_researcher
# # Import new agent creation functions here
# from app.workflows.single import AgentRunEvent, AgentRunResult, FunctionCallingAgent
# from llama_index.core.chat_engine.types import ChatMessage
# from llama_index.core.prompts import PromptTemplate
# from llama_index.core.settings import Settings
# from llama_index.core.workflow import (
#     Context,
#     Event,
#     StartEvent,
#     StopEvent,
#     Workflow,
#     step,
# )


# def create_workflow(chat_history: Optional[List[ChatMessage]] = None, **kwargs):
#     researcher = create_researcher(
#         chat_history=chat_history,
#         **kwargs,
#     )

#     # problem definition
#     user_proxy = create_user_proxy(chat_history=chat_history)
#     analyst = create_analyst(chat_history=chat_history)

#     # initial research
#     reporter = create_reporter(chat_history=chat_history)

#     workflow = FinancialReportWorkflow(timeout=360, chat_history=chat_history)

#     workflow.add_workflows(
#         researcher=researcher,
#         analyst=analyst,
#         reporter=reporter,
#     )
#     return workflow


# class ResearchEvent(Event):
#     input: str


# class AnalyzeEvent(Event):
#     input: str


# class ReportEvent(Event):
#     input: str


# class FinancialReportWorkflow(Workflow):
#     def __init__(
#         self, timeout: int = 360, chat_history: Optional[List[ChatMessage]] = None
#     ):
#         super().__init__(timeout=timeout)
#         self.chat_history = chat_history or []

#     @step()
#     async def start(self, ctx: Context, ev: StartEvent) -> ResearchEvent | ReportEvent:
#         # set streaming
#         ctx.data["streaming"] = getattr(ev, "streaming", False)
#         # start the workflow with researching about a topic
#         ctx.data["task"] = ev.input
#         ctx.data["user_input"] = ev.input

#         # Decision-making process
#         decision = await self._decide_workflow(ev.input, self.chat_history)

#         if decision != "publish":
#             return ResearchEvent(input=f"Research for this task: {ev.input}")
#         else:
#             chat_history_str = "\n".join(
#                 [f"{msg.role}: {msg.content}" for msg in self.chat_history]
#             )
#             return ReportEvent(
#                 input=f"Create a report based on the chat history\n{chat_history_str}\n\n and task: {ev.input}"
#             )

#     async def _decide_workflow(
#         self, input: str, chat_history: List[ChatMessage]
#     ) -> str:
#         # TODO: Refactor this by using prompt generation
#         prompt_template = PromptTemplate(
#             dedent(
#                 """
#                 You are an expert in decision-making, helping people create financial reports for the provided data.
#                 If the user doesn't need to add or update anything, respond with 'publish'.
#                 Otherwise, respond with 'research'.

#                 Here is the chat history:
#                 {chat_history}

#                 The current user request is:
#                 {input}

#                 Given the chat history and the new user request, decide whether to create a report based on existing information.
#                 Decision (respond with either 'not_publish' or 'publish'):
#             """
#             )
#         )

#         chat_history_str = "\n".join(
#             [f"{msg.role}: {msg.content}" for msg in chat_history]
#         )
#         prompt = prompt_template.format(chat_history=chat_history_str, input=input)

#         output = await Settings.llm.acomplete(prompt)
#         decision = output.text.strip().lower()

#         return "publish" if decision == "publish" else "research"

#     @step()
#     async def research(
#         self, ctx: Context, ev: ResearchEvent, researcher: FunctionCallingAgent
#     ) -> AnalyzeEvent:
#         result: AgentRunResult = await self.run_agent(ctx, researcher, ev.input)
#         content = result.response.message.content
#         return AnalyzeEvent(
#             input=dedent(
#                 f"""
#                 Given the following research content:
#                 {content}
#                 Provide a comprehensive analysis of the data for the user's request: {ctx.data["task"]}
#                 """
#             )
#         )

#     @step()
#     async def analyze(
#         self, ctx: Context, ev: AnalyzeEvent, analyst: FunctionCallingAgent
#     ) -> ReportEvent | StopEvent:
#         result: AgentRunResult = await self.run_agent(ctx, analyst, ev.input)
#         content = result.response.message.content
#         return ReportEvent(
#             input=dedent(
#                 f"""
#                 Given the following analysis:
#                 {content}
#                 Create a report for the user's request: {ctx.data["task"]}
#                 """
#             )
#         )

#     @step()
#     async def report(
#         self, ctx: Context, ev: ReportEvent, reporter: FunctionCallingAgent
#     ) -> StopEvent:
#         try:
#             result: AgentRunResult = await self.run_agent(
#                 ctx, reporter, ev.input, streaming=ctx.data["streaming"]
#             )
#             return StopEvent(result=result)
#         except Exception as e:
#             ctx.write_event_to_stream(
#                 AgentRunEvent(
#                     name=reporter.name,
#                     msg=f"Error creating a report: {e}",
#                 )
#             )
#             return StopEvent(result=None)

#     async def run_agent(
#         self,
#         ctx: Context,
#         agent: FunctionCallingAgent,
#         input: str,
#         streaming: bool = False,
#     ) -> AgentRunResult | AsyncGenerator:
#         handler = agent.run(input=input, streaming=streaming)
#         # bubble all events while running the executor to the planner
#         async for event in handler.stream_events():
#             # Don't write the StopEvent from sub task to the stream
#             if type(event) is not StopEvent:
#                 ctx.write_event_to_stream(event)
#         return await handler


# class IdeaValidationStage(Enum):
#     PROBLEM_DEFINITION = "problem_definition"
#     INITIAL_RESEARCH = "initial_research"
#     REVIEW_REFINE = "review_refine"
#     POST_RESEARCH = "post_research"
#     POST_RESEARCH_REVIEW = "post_research_review"
#     FINAL_OUTPUT = "final_output"

# class IdeaValidationEvent(Event):
#     stage: IdeaValidationStage
#     input: str

# def create_idea_validation_workflow(chat_history: Optional[List[ChatMessage]] = None, **kwargs):
#     # Create all the necessary agents here
#     problem_definition_agent = create_problem_definition_agent(chat_history=chat_history, **kwargs)
#     critic_agent = create_critic_agent(chat_history=chat_history, **kwargs)
    
#     # Initial Research Team
#     market_research_agent = create_market_research_agent(chat_history=chat_history, **kwargs)
#     competitor_analysis_agent = create_competitor_analysis_agent(chat_history=chat_history, **kwargs)
#     customer_insights_agent = create_customer_insights_agent(chat_history=chat_history, **kwargs)
#     trends_research_agent = create_trends_research_agent(chat_history=chat_history, **kwargs)
    
#     # Review & Refine
#     reviewer_refiner_agent = create_reviewer_refiner_agent(chat_history=chat_history, **kwargs)
    
#     # Post-Research Team
#     risk_analysis_agent = create_risk_analysis_agent(chat_history=chat_history, **kwargs)
#     monetization_agent = create_monetization_agent(chat_history=chat_history, **kwargs)
#     gtm_strategy_agent = create_gtm_strategy_agent(chat_history=chat_history, **kwargs)
    
#     # Post-Research Review Team
#     technical_feasibility_agent = create_technical_feasibility_agent(chat_history=chat_history, **kwargs)
#     financial_feasibility_agent = create_financial_feasibility_agent(chat_history=chat_history, **kwargs)
#     operational_feasibility_agent = create_operational_feasibility_agent(chat_history=chat_history, **kwargs)
    
#     # Final Output
#     podcast_summary_agent = create_podcast_summary_agent(chat_history=chat_history, **kwargs)
#     summarizer_agent = create_summarizer_agent(chat_history=chat_history, **kwargs)
#     landing_page_design_agent = create_landing_page_design_agent(chat_history=chat_history, **kwargs)

#     workflow = IdeaValidationWorkflow(timeout=3600, chat_history=chat_history)

#     workflow.add_workflows(
#         problem_definition=problem_definition_agent,
#         critic=critic_agent,
#         market_research=market_research_agent,
#         competitor_analysis=competitor_analysis_agent,
#         customer_insights=customer_insights_agent,
#         trends_research=trends_research_agent,
#         reviewer_refiner=reviewer_refiner_agent,
#         risk_analysis=risk_analysis_agent,
#         monetization=monetization_agent,
#         gtm_strategy=gtm_strategy_agent,
#         technical_feasibility=technical_feasibility_agent,
#         financial_feasibility=financial_feasibility_agent,
#         operational_feasibility=operational_feasibility_agent,
#         podcast_summary=podcast_summary_agent,
#         summarizer=summarizer_agent,
#         landing_page_design=landing_page_design_agent,
#     )
#     return workflow

# class IdeaValidationWorkflow(Workflow):
#     def __init__(
#         self, timeout: int = 3600, chat_history: Optional[List[ChatMessage]] = None
#     ):
#         super().__init__(timeout=timeout)
#         self.chat_history = chat_history or []
#         self.research_results: Dict[str, str] = {}

#     @step()
#     async def start(self, ctx: Context, ev: StartEvent) -> IdeaValidationEvent:
#         ctx.data["streaming"] = getattr(ev, "streaming", False)
#         ctx.data["idea"] = ev.input
#         return IdeaValidationEvent(stage=IdeaValidationStage.PROBLEM_DEFINITION, input=ev.input)

#     @step()
#     async def problem_definition(
#         self, ctx: Context, ev: IdeaValidationEvent, problem_definition: FunctionCallingAgent, critic: FunctionCallingAgent
#     ) -> IdeaValidationEvent:
#         result = await self.run_agent(ctx, problem_definition, ev.input)
#         critique = await self.run_agent(ctx, critic, result.response.message.content)
        
#         if critique.response.message.content.lower().startswith("approved"):
#             return IdeaValidationEvent(stage=IdeaValidationStage.INITIAL_RESEARCH, input=result.response.message.content)
#         else:
#             return IdeaValidationEvent(stage=IdeaValidationStage.PROBLEM_DEFINITION, input=f"{ev.input}\nCritique: {critique.response.message.content}")

#     @step()
#     async def initial_research(
#         self, ctx: Context, ev: IdeaValidationEvent, 
#         market_research: FunctionCallingAgent, competitor_analysis: FunctionCallingAgent, 
#         customer_insights: FunctionCallingAgent, trends_research: FunctionCallingAgent,
#         critic: FunctionCallingAgent
#     ) -> IdeaValidationEvent:
#         research_tasks = {
#             "market_research": market_research,
#             "competitor_analysis": competitor_analysis,
#             "customer_insights": customer_insights,
#             "trends_research": trends_research,
#         }
        
#         for task, agent in research_tasks.items():
#             result = await self.run_agent(ctx, agent, ev.input)
#             critique = await self.run_agent(ctx, critic, result.response.message.content)
            
#             if critique.response.message.content.lower().startswith("approved"):
#                 self.research_results[task] = result.response.message.content
#             else:
#                 return IdeaValidationEvent(stage=IdeaValidationStage.INITIAL_RESEARCH, input=f"{ev.input}\nTask: {task}\nCritique: {critique.response.message.content}")
        
#         return IdeaValidationEvent(stage=IdeaValidationStage.REVIEW_REFINE, input=str(self.research_results))

#     @step()
#     async def review_refine(
#         self, ctx: Context, ev: IdeaValidationEvent, reviewer_refiner: FunctionCallingAgent
#     ) -> IdeaValidationEvent:
#         result = await self.run_agent(ctx, reviewer_refiner, ev.input)
#         refined_idea = result.response.message.content
        
#         if "REFINE" in refined_idea.upper():
#             return IdeaValidationEvent(stage=IdeaValidationStage.INITIAL_RESEARCH, input=refined_idea)
#         else:
#             return IdeaValidationEvent(stage=IdeaValidationStage.POST_RESEARCH, input=refined_idea)

#     @step()
#     async def post_research(
#         self, ctx: Context, ev: IdeaValidationEvent,
#         risk_analysis: FunctionCallingAgent, monetization: FunctionCallingAgent,
#         gtm_strategy: FunctionCallingAgent, critic: FunctionCallingAgent
#     ) -> IdeaValidationEvent:
#         research_tasks = {
#             "risk_analysis": risk_analysis,
#             "monetization": monetization,
#             "gtm_strategy": gtm_strategy,
#         }
        
#         for task, agent in research_tasks.items():
#             result = await self.run_agent(ctx, agent, ev.input)
#             critique = await self.run_agent(ctx, critic, result.response.message.content)
            
#             if critique.response.message.content.lower().startswith("approved"):
#                 self.research_results[task] = result.response.message.content
#             else:
#                 return IdeaValidationEvent(stage=IdeaValidationStage.POST_RESEARCH, input=f"{ev.input}\nTask: {task}\nCritique: {critique.response.message.content}")
        
#         return IdeaValidationEvent(stage=IdeaValidationStage.POST_RESEARCH_REVIEW, input=str(self.research_results))

#     @step()
#     async def post_research_review(
#         self, ctx: Context, ev: IdeaValidationEvent,
#         technical_feasibility: FunctionCallingAgent, financial_feasibility: FunctionCallingAgent,
#         operational_feasibility: FunctionCallingAgent, critic: FunctionCallingAgent
#     ) -> IdeaValidationEvent:
#         research_tasks = {
#             "technical_feasibility": technical_feasibility,
#             "financial_feasibility": financial_feasibility,
#             "operational_feasibility": operational_feasibility,
#         }
        
#         for task, agent in research_tasks.items():
#             result = await self.run_agent(ctx, agent, ev.input)
#             critique = await self.run_agent(ctx, critic, result.response.message.content)
            
#             if critique.response.message.content.lower().startswith("approved"):
#                 self.research_results[task] = result.response.message.content
#             else:
#                 return IdeaValidationEvent(stage=IdeaValidationStage.POST_RESEARCH_REVIEW, input=f"{ev.input}\nTask: {task}\nCritique: {critique.response.message.content}")
        
#         return IdeaValidationEvent(stage=IdeaValidationStage.FINAL_OUTPUT, input=str(self.research_results))

#     @step()
#     async def final_output(
#         self, ctx: Context, ev: IdeaValidationEvent,
#         podcast_summary: FunctionCallingAgent, summarizer: FunctionCallingAgent,
#         landing_page_design: FunctionCallingAgent
#     ) -> StopEvent:
#         podcast_result = await self.run_agent(ctx, podcast_summary, ev.input)
#         summary_result = await self.run_agent(ctx, summarizer, ev.input)
#         landing_page_result = await self.run_agent(ctx, landing_page_design, ev.input)
        
#         final_output = {
#             "podcast_summary": podcast_result.response.message.content,
#             "executive_summary": summary_result.response.message.content,
#             "landing_page_design": landing_page_result.response.message.content,
#         }
        
#         return StopEvent(result=final_output)

#     async def run_agent(
#         self,
#         ctx: Context,
#         agent: FunctionCallingAgent,
#         input: str,
#         streaming: bool = False,
#     ) -> AgentRunResult | AsyncGenerator:
#         handler = agent.run(input=input, streaming=streaming)
#         async for event in handler.stream_events():
#             if type(event) is not StopEvent:
#                 ctx.write_event_to_stream(event)
#         return await handler

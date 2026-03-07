import os
import sys

def test_system_integrity():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    agents_dir = os.path.join(base, 'agents')
    workflows_dir = os.path.join(base, 'workflows')
    skills_dir = os.path.join(base, 'skills')
    rules_file = os.path.join(base, 'rules', 'GEMINI.md')
    
    errors = []
    
    # 1. Test Agents
    print('Testing Agents...')
    agents = [f for f in os.listdir(agents_dir) if f.endswith('.md')]
    if len(agents) == 0:
        errors.append('No agents found!')
    
    for agent in agents:
        with open(os.path.join(agents_dir, agent), 'r', encoding='utf-8') as f:
            content = f.read()
            if 'skills:' not in content:
                errors.append(f'Agent {agent} is missing skills array')
            
    # 2. Test Workflows
    print('Testing Workflows...')
    workflows = [f for f in os.listdir(workflows_dir) if f.endswith('.md')]
    core_wfs = {
        'boss.md', 'day.md', 'track.md', 'meet.md', 'create.md',
        'plan.md', 'retro.md', 'vacuum.md', 'fan-out.md', 'sprint.md',
        'discover.md', 'prioritize.md', 'paste.md', 'help.md', 'review.md',
        'data.md', 'launch.md', 'bug.md', 'feature-kickoff.md', 'regression.md'
    }
    
    for wf in workflows:
        if wf not in core_wfs and wf != 'archive':
            pass
        # Ensure templates were removed (strict check)
        with open(os.path.join(workflows_dir, wf), 'r', encoding='utf-8') as f:
            if '```markdown\n#' in f.read():
                errors.append(f'Workflow {wf} still contains embedded markdown templates. It is bloated.')
                
    # 3. Test Skills
    print('Testing Skills...')
    skills = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]
    for skill in skills:
        skill_path = os.path.join(skills_dir, skill)
        if not os.path.exists(os.path.join(skill_path, 'SKILL.md')):
             errors.append(f'Skill {skill} missing SKILL.md')
        if not os.path.exists(os.path.join(skill_path, 'assets')):
             errors.append(f'Skill {skill} missing assets directory')
             
    # 4. Rules Integrity
    print('Testing Rules Anchor...')
    with open(rules_file, 'r', encoding='utf-8') as f:
        rules_text = f.read()
        if '## 🚀 TIER 0.5: THREE-TIER ARCHITECTURE' not in rules_text:
            errors.append('GEMINI.md missing the Three-Tier Architecture anchor.')

    print('\n--- TEST RESULTS ---')
    if errors:
        for err in errors:
            print(f'❌ ERROR: {err}')
        sys.exit(1)
    else:
        print('✅ ALL TESTS PASSED. System Integrity is at 100%.')
        print(f'Detected: {len(agents)} Agents, {len(workflows)} Workflows, {len(skills)} Skills.')

if __name__ == "__main__":
    test_system_integrity()
